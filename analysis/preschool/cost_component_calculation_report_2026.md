# Preschool Cost Component Calculation Report 2026

## Purpose

This report explains exactly how each preschool cost component is calculated in the current workspace model, including formulas and assumptions used for ranking and financial scenarios.

## Primary Data Sources

- Candidate table with embedded formulas:
  - `planning/preschool_candidates_extracted_provisional.csv`
- Methodology notes:
  - `analysis/preschool/ranking_methodology_2026.md`
  - `planning/preschool_rating_rubric.md`

## Cost Components and Formulas

All currency values are in Indonesian Rupiah (IDR).

1. Monthly Tuition (`Monthly_SPP_IDR`)
- Meaning: recurring monthly tuition fee.
- Source column: `D`
- Formula: direct input from brochure extraction.

2. Annual Fee (`Annual_Fee_IDR`)
- Meaning: annual recurring fee converted to monthly equivalent when computing effective monthly opex.
- Source column: `E`
- Formula use in monthly opex: `Annual_Fee_IDR / 12`

3. Registration (`Registration_IDR`)
- Meaning: one-time enrollment/registration fee.
- Source column: `F`
- Formula: direct input, included in 2-year total.

4. One-Time Fee (`One_Time_Fee_IDR`)
- Meaning: upfront non-recurring fee (for example development/building package depending on school).
- Source column: `G`
- Formula: direct input, included in 2-year total.

5. Monthly Transport (`Monthly_Transport_IDR`)
- Meaning: estimated monthly commute cost from fixed home base.
- Inputs:
  - `Distance_OneWay_KM` (column `H`)
  - `Transport_Cost_per_KM_IDR` (column `I`, fixed at 2,500)
  - `School_Days_Per_Month` (column `J`, fixed at 22)
- CSV formula (`K`):
  - `=Hn*2*In*Jn`
- Mathematical form:
  - $\text{MonthlyTransport} = \text{DistanceOneWayKm} \times 2 \times \text{CostPerKm} \times \text{SchoolDaysPerMonth}$

6. Monthly Opex Effective (`Monthly_Opex_Effective_IDR`)
- Meaning: normalized monthly education operating cost for comparison.
- Inputs:
  - `Monthly_SPP_IDR` (column `D`)
  - `Annual_Fee_IDR` (column `E`)
  - `Monthly_Transport_IDR` (column `K`)
- CSV formula (`L`):
  - `=Dn+(En/12)+Kn`
- Mathematical form:
  - $\text{MonthlyOpexEffective} = \text{MonthlySPP} + \frac{\text{AnnualFee}}{12} + \text{MonthlyTransport}$

7. Two-Year Total (`Two_Year_Total_IDR`)
- Meaning: total expected spend for TK-A plus TK-B within current model.
- Inputs:
  - `Registration_IDR` (column `F`)
  - `One_Time_Fee_IDR` (column `G`)
  - `Annual_Fee_IDR` (column `E`)
  - `Monthly_SPP_IDR` (column `D`)
  - `Monthly_Transport_IDR` (column `K`)
- CSV formula (`M`):
  - `=Fn+Gn+(En*2)+(Dn*24)+(Kn*24)`
- Mathematical form:
  - $$
    \text{TwoYearTotal} = \text{Registration} + \text{OneTimeFee} + (2 \times \text{AnnualFee}) + (24 \times \text{MonthlySPP}) + (24 \times \text{MonthlyTransport})
    $$

## Derived Cost Scores (for ranking)

1. Cost Rating (`Cost_Rating_1to5`, column `O`)
- Formula:
  - `=ROUND(5*((MIN(L_range)/Ln)*0.4 + (MIN(M_range)/Mn)*0.6),2)`
- Interpretation:
  - 40% weight: monthly affordability competitiveness.
  - 60% weight: total 2-year affordability competitiveness.
  - Lower cost produces higher rating.

2. Cost Score (0-100, methodology file)
- Formula:
  - $\text{CostScore} = 100 \times (0.4 \times \min(\text{MonthlyCost})/\text{MonthlyCost} + 0.3 \times \min(\text{Year1Cost})/\text{Year1Cost} + 0.3 \times \min(\text{Year2Cost})/\text{Year2Cost})$
- Used in `analysis/preschool/ranking_methodology_2026.md` for quality/cost/optimized ranking outputs.

## Key Assumptions (Current Model)

- Transport cost per km fixed at IDR 2,500.
- School days per month fixed at 22.
- Home base fixed to Pekayon Jaya (see `data/context/home_base_and_rules.md`).
- Continuity assumption (seat priority and potential 30% discount for elementary progression) is documented as note only and excluded from scoring formulas.
- Extracted values are provisional until brochure/web validation is complete.

## Worked Example Template (per school)

Use this checklist while validating latest costs:

1. Confirm raw fee inputs from source:
- Monthly SPP
- Annual fee
- Registration fee
- One-time fee

2. Confirm distance and compute transport:
- One-way km x 2 x 2,500 x 22

3. Compute monthly effective opex:
- Monthly SPP + (annual fee / 12) + monthly transport

4. Compute 2-year total:
- Registration + one-time + (annual fee x 2) + (monthly SPP x 24) + (monthly transport x 24)

5. Recompute comparative cost rating after all schools are updated.

## Next-Step Readiness for Scraping

For the next phase (latest cost scraping for top-3 of each ranking), collect for each target school:

- Fee schedule date/effective year
- Tuition (monthly/term/yearly) and conversion rule
- Annual/administrative fees
- Registration and one-time fees
- Program scope included in each fee
- Source URL and snapshot timestamp

This ensures recalculation is reproducible and auditable.