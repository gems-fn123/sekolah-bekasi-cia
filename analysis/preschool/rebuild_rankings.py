from __future__ import annotations

import argparse
import csv
from pathlib import Path

import pandas as pd

INPUT_DEFAULT = Path("planning/preschool_candidates_extracted_provisional.csv")
OUTPUT_DIR_DEFAULT = Path("outputs/tables")
HOME_BASE_ADDRESS = (
    "Jl. Pulo Sirih Timur 3 Blok CA No.8, RT.006/RW.013, Pekayon Jaya, "
    "Bekasi Selatan, Bekasi, West Java 17148"
)
HOME_PLUS_CODE = "PXMF+XQ Pekayon Jaya, Bekasi, West Java"
CONTINUITY_NOTE = (
    "Graduates generally get seat and discount (assumed 30%) for elementary; "
    "not used in current ranking scores"
)


def _to_float(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").fillna(0.0)


def load_candidates(path: Path) -> pd.DataFrame:
    expected_columns = {
        "School",
        "Curriculum_Rating_1to5",
        "Languages_Rating_1to5",
        "Monthly_SPP_IDR",
        "Annual_Fee_IDR",
        "Registration_IDR",
        "One_Time_Fee_IDR",
        "Distance_OneWay_KM",
        "Transport_Cost_per_KM_IDR",
        "School_Days_Per_Month",
        "Continuity_Bonus_0to1",
    }

    try:
        df = pd.read_csv(path)
        if not expected_columns.issubset(set(df.columns)):
            raise ValueError("missing expected columns")
    except Exception:
        records: list[dict[str, str]] = []
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            header = next(reader, None)
            if not header:
                raise ValueError(f"Candidate CSV is empty: {path}")

            for row in reader:
                if not row:
                    continue
                if len(row) == 17:
                    (
                        school,
                        curriculum,
                        languages,
                        monthly_spp,
                        annual_fee,
                        registration,
                        one_time,
                        distance,
                        transport_per_km,
                        school_days,
                        monthly_transport,
                        monthly_opex,
                        two_year_total,
                        continuity_bonus,
                        cost_rating,
                        final_score,
                        notes,
                    ) = row
                elif len(row) == 19:
                    (
                        school,
                        curriculum,
                        languages,
                        monthly_spp,
                        annual_fee,
                        registration,
                        one_time,
                        distance,
                        transport_per_km,
                        school_days,
                        monthly_transport,
                        monthly_opex,
                        two_year_total,
                        continuity_bonus,
                        cost_rating_a,
                        cost_rating_b,
                        final_score_a,
                        final_score_b,
                        notes,
                    ) = row
                    cost_rating = f"{cost_rating_a},{cost_rating_b}"
                    final_score = f"{final_score_a},{final_score_b}"
                else:
                    raise ValueError(f"Unexpected column count ({len(row)}) in {path}: {row[:3]}...")

                records.append(
                    {
                        "School": school,
                        "Curriculum_Rating_1to5": curriculum,
                        "Languages_Rating_1to5": languages,
                        "Monthly_SPP_IDR": monthly_spp,
                        "Annual_Fee_IDR": annual_fee,
                        "Registration_IDR": registration,
                        "One_Time_Fee_IDR": one_time,
                        "Distance_OneWay_KM": distance,
                        "Transport_Cost_per_KM_IDR": transport_per_km,
                        "School_Days_Per_Month": school_days,
                        "Monthly_Transport_IDR": monthly_transport,
                        "Monthly_Opex_Effective_IDR": monthly_opex,
                        "Two_Year_Total_IDR": two_year_total,
                        "Continuity_Bonus_0to1": continuity_bonus,
                        "Cost_Rating_1to5": cost_rating,
                        "Final_Score_100": final_score,
                        "Notes": notes,
                    }
                )

        df = pd.DataFrame(records)

    numeric_cols = [
        "Curriculum_Rating_1to5",
        "Languages_Rating_1to5",
        "Monthly_SPP_IDR",
        "Annual_Fee_IDR",
        "Registration_IDR",
        "One_Time_Fee_IDR",
        "Distance_OneWay_KM",
        "Transport_Cost_per_KM_IDR",
        "School_Days_Per_Month",
        "Continuity_Bonus_0to1",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = _to_float(df[col])
        else:
            df[col] = 0.0

    return df


def compute_scores(df: pd.DataFrame) -> pd.DataFrame:
    # Cost components
    df = df.copy()
    df["Monthly_Transport_IDR"] = (
        df["Distance_OneWay_KM"] * 2 * df["Transport_Cost_per_KM_IDR"] * df["School_Days_Per_Month"]
    )
    df["Monthly_Cost_IDR"] = (
        df["Monthly_SPP_IDR"] + (df["Annual_Fee_IDR"] / 12.0) + df["Monthly_Transport_IDR"]
    )
    df["Year1_Cost_IDR"] = (
        df["Monthly_Cost_IDR"] * 12 + df["Registration_IDR"] + df["One_Time_Fee_IDR"]
    )
    df["Year2_Cost_IDR"] = df["Monthly_Cost_IDR"] * 12
    df["TwoYear_Total_IDR"] = df["Year1_Cost_IDR"] + df["Year2_Cost_IDR"]

    # Scores (continuity intentionally excluded from ranking scores)
    df["Quality_Score_100"] = (
        ((df["Curriculum_Rating_1to5"] / 5.0) * 35 + ((df["Languages_Rating_1to5"] / 5.0) * 20)) / 55.0
    ) * 100.0

    min_monthly = df["Monthly_Cost_IDR"].min()
    min_year1 = df["Year1_Cost_IDR"].min()
    min_year2 = df["Year2_Cost_IDR"].min()

    df["Cost_Score_100"] = 100.0 * (
        0.4 * (min_monthly / df["Monthly_Cost_IDR"])
        + 0.3 * (min_year1 / df["Year1_Cost_IDR"])
        + 0.3 * (min_year2 / df["Year2_Cost_IDR"])
    )

    df["Optimized_Score_100"] = (
        (
            ((df["Curriculum_Rating_1to5"] / 5.0) * 35)
            + ((df["Languages_Rating_1to5"] / 5.0) * 20)
            + ((df["Cost_Score_100"] / 100.0) * 35)
        )
        / 90.0
    ) * 100.0

    for col in ["Quality_Score_100", "Cost_Score_100", "Optimized_Score_100"]:
        df[col] = df[col].round(2)

    # backward-compatible helper metric
    df["Cost_Rating_1to5"] = (df["Cost_Score_100"] / 20.0).round(2)

    return df


def build_outputs(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    quality_sorted = df.sort_values(["Quality_Score_100", "Cost_Score_100"], ascending=[False, False]).reset_index(drop=True)
    quality_sorted.insert(0, "Rank", quality_sorted.index + 1)

    cost_sorted = df.sort_values(["Cost_Score_100", "Quality_Score_100"], ascending=[False, False]).reset_index(drop=True)
    cost_sorted.insert(0, "Rank", cost_sorted.index + 1)

    optimized_sorted = df.sort_values(["Optimized_Score_100", "Quality_Score_100"], ascending=[False, False]).reset_index(drop=True)
    optimized_sorted.insert(0, "Rank", optimized_sorted.index + 1)

    rank_map_quality = quality_sorted.set_index("School")["Rank"]
    rank_map_cost = cost_sorted.set_index("School")["Rank"]
    rank_map_optimized = optimized_sorted.set_index("School")["Rank"]

    comprehensive = df.copy()
    comprehensive["Quality_Rank"] = comprehensive["School"].map(rank_map_quality)
    comprehensive["Cost_Rank"] = comprehensive["School"].map(rank_map_cost)
    comprehensive["Optimized_Rank"] = comprehensive["School"].map(rank_map_optimized)
    comprehensive["Home_Base_Address"] = HOME_BASE_ADDRESS
    comprehensive["Home_Plus_Code"] = HOME_PLUS_CODE
    comprehensive["Continuity_Note"] = CONTINUITY_NOTE

    keep_cols = [
        "School",
        "Curriculum_Rating_1to5",
        "Languages_Rating_1to5",
        "Monthly_Cost_IDR",
        "Year1_Cost_IDR",
        "Year2_Cost_IDR",
        "TwoYear_Total_IDR",
        "Quality_Score_100",
        "Cost_Score_100",
        "Optimized_Score_100",
        "Quality_Rank",
        "Cost_Rank",
        "Optimized_Rank",
        "Home_Base_Address",
        "Home_Plus_Code",
        "Continuity_Note",
    ]
    comprehensive = comprehensive[keep_cols].sort_values("Optimized_Rank").reset_index(drop=True)
    for col in ["Monthly_Cost_IDR", "Year1_Cost_IDR", "Year2_Cost_IDR", "TwoYear_Total_IDR"]:
        comprehensive[col] = comprehensive[col].round(0).astype(int)
    for col in ["Quality_Rank", "Cost_Rank", "Optimized_Rank"]:
        comprehensive[col] = comprehensive[col].astype(int)

    optimized_view = optimized_sorted[
        [
            "Rank",
            "School",
            "Optimized_Score_100",
            "Quality_Score_100",
            "Cost_Score_100",
            "Monthly_Cost_IDR",
            "Year1_Cost_IDR",
            "Year2_Cost_IDR",
        ]
    ]

    quality_view = quality_sorted[
        ["Rank", "School", "Quality_Score_100", "Cost_Score_100", "Optimized_Score_100", "Monthly_Cost_IDR", "Year1_Cost_IDR", "Year2_Cost_IDR"]
    ]

    cost_view = cost_sorted[
        ["Rank", "School", "Cost_Score_100", "Quality_Score_100", "Optimized_Score_100", "Monthly_Cost_IDR", "Year1_Cost_IDR", "Year2_Cost_IDR"]
    ]

    for view in [optimized_view, quality_view, cost_view]:
        for col in ["Monthly_Cost_IDR", "Year1_Cost_IDR", "Year2_Cost_IDR"]:
            view[col] = view[col].round(0).astype(int)

    return comprehensive, quality_view, cost_view, optimized_view


def write_tables(output_dir: Path, comprehensive: pd.DataFrame, quality: pd.DataFrame, cost: pd.DataFrame, optimized: pd.DataFrame) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    comprehensive.to_csv(output_dir / "preschool_rankings_comprehensive.csv", index=False)
    quality.to_csv(output_dir / "preschool_rank_quality.csv", index=False)
    cost.to_csv(output_dir / "preschool_rank_cost.csv", index=False)
    optimized.to_csv(output_dir / "preschool_rank_optimized.csv", index=False)


def write_normalized_candidates(df: pd.DataFrame, path: Path) -> None:
    out = df[
        [
            "School",
            "Curriculum_Rating_1to5",
            "Languages_Rating_1to5",
            "Monthly_SPP_IDR",
            "Annual_Fee_IDR",
            "Registration_IDR",
            "One_Time_Fee_IDR",
            "Distance_OneWay_KM",
            "Transport_Cost_per_KM_IDR",
            "School_Days_Per_Month",
            "Monthly_Transport_IDR",
            "Monthly_Cost_IDR",
            "Year1_Cost_IDR",
            "Year2_Cost_IDR",
            "TwoYear_Total_IDR",
            "Continuity_Bonus_0to1",
            "Cost_Rating_1to5",
            "Quality_Score_100",
            "Cost_Score_100",
            "Optimized_Score_100",
            "Notes",
        ]
    ].copy()

    int_like_cols = [
        "Monthly_SPP_IDR",
        "Annual_Fee_IDR",
        "Registration_IDR",
        "One_Time_Fee_IDR",
        "Transport_Cost_per_KM_IDR",
        "School_Days_Per_Month",
        "Monthly_Transport_IDR",
        "Monthly_Cost_IDR",
        "Year1_Cost_IDR",
        "Year2_Cost_IDR",
        "TwoYear_Total_IDR",
    ]
    for col in int_like_cols:
        out[col] = out[col].round(0).astype(int)

    out.to_csv(path, index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild preschool ranking tables from candidate extraction dataset")
    parser.add_argument("--input", default=str(INPUT_DEFAULT), help="Path to candidate extraction CSV")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR_DEFAULT), help="Directory for ranking tables")
    parser.add_argument(
        "--write-candidates",
        action="store_true",
        help="Overwrite candidate extraction CSV with normalized numeric fields",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)

    candidates = load_candidates(input_path)
    scored = compute_scores(candidates)
    comprehensive, quality, cost, optimized = build_outputs(scored)
    write_tables(output_dir, comprehensive, quality, cost, optimized)

    if args.write_candidates:
        write_normalized_candidates(scored, input_path)

    print(f"Rebuilt ranking tables in {output_dir}")


if __name__ == "__main__":
    main()
