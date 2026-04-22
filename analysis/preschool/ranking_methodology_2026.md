# Preschool Ranking Methodology 2026

## Inputs used
- School fee and rating inputs extracted from brochure snapshots in this repository.
- Home base fixed to Pekayon Jaya address in data/context/home_base_and_rules.md.
- Transport model:
  - Monthly transport = one-way distance x 2 x 22 days x Rp 2,500 per km
- Ranking tables are rebuilt from source candidates via:
  - `python analysis/preschool/rebuild_rankings.py --write-candidates`

## Cost normalization outputs
For each school, these are generated:
- Monthly Cost
- Year-1 Cost = (Monthly Cost x 12) + Registration + One-Time Cost
- Year-2 Cost = Monthly Cost x 12

## Scores
1. Quality Score (0-100)
- Uses only curriculum and languages:
- QualityScore = ((Curriculum/5 x 35) + (Languages/5 x 20)) / 55 x 100

2. Cost Score (0-100)
- Higher score means more affordable.
- CostScore = 100 x (0.4 x min(MonthlyCost)/MonthlyCost + 0.3 x min(Year1Cost)/Year1Cost + 0.3 x min(Year2Cost)/Year2Cost)

3. Optimized Score (0-100)
- Uses agreed fractions with continuity excluded from ratings:
- OptimizedScore = ((Curriculum/5 x 35) + (Languages/5 x 20) + (CostScore/100 x 35)) / 90 x 100

## Continuity note policy
- Seat priority and 30% discount assumption for same-school Elementary progression is recorded as note only.
- It is not included in Quality, Cost, or Optimized scoring.

## Consistency guardrail
- Do not use spreadsheet formulas embedded in CSV cells as system-of-record values.
- Use the rebuilt numeric candidate file and generated tables under `outputs/tables/` as the downstream source for dashboards/BI.
