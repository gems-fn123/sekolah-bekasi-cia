# Preschool Rating Rubric (TK-A and TK-B)

## Weight Setup
- Curriculum: 35%
- Languages: 20%
- Cost efficiency (monthly plus 2-year total): 35%
- Continuity bonus to Elementary in same environment: documented as note only (excluded from ranking score)

## Curriculum Rating (1 to 5)
- 5: Proven child-centered curriculum, strong literacy-numeracy readiness, project-based learning, and clear parent progress reporting.
- 4: Structured curriculum with measurable outcomes and regular progress reports.
- 3: Basic curriculum coverage with limited evidence of learning outcomes.
- 2: Curriculum exists but is inconsistent or weakly implemented.
- 1: No clear curriculum clarity for TK-A and TK-B progression.

## Languages Rating (1 to 5)
- 5: Strong bilingual exposure (daily) with age-appropriate speaking, listening, and early literacy.
- 4: Consistent dual-language sessions each week with clear progression.
- 3: One additional language introduced but not consistently reinforced.
- 2: Language exposure is occasional and mostly extracurricular.
- 1: No clear language development plan.

## Cost Rating (1 to 5)
- Automatically calculated in the CSV using lower cost as better.
- Uses both monthly opex and 2-year TK-A plus TK-B total:
  - 40% weight on monthly opex competitiveness.
  - 60% weight on 2-year total competitiveness.

## Continuity Bonus (0 to 1)
- 1.0: Clear continuity path to Elementary in same school/environment with priority seat.
- 0.5: Same foundation but different campus and no guaranteed continuation.
- 0.0: No continuity pathway.
- This field is retained for scenario notes and future what-if analysis, but is currently excluded from ranking scores.

## Cost Formula Notes
- Monthly transport = one-way distance x 2 x cost per km x school days per month.
- Monthly opex = tuition + extra monthly fees + monthly transport.
- Yearly total = monthly opex x 12.
- 2-year total = yearly total x 2.

## Final Score Formula
Final score is out of 100:
- `QualityScore = ((Curriculum/5 x 35) + (Languages/5 x 20)) / 55 x 100`
- `CostScore = 100 x (0.4 x min(MonthlyCost)/MonthlyCost + 0.3 x min(Year1Cost)/Year1Cost + 0.3 x min(Year2Cost)/Year2Cost)`
- `OptimizedScore = ((Curriculum/5 x 35) + (Languages/5 x 20) + (CostScore/100 x 35)) / 90 x 100`
