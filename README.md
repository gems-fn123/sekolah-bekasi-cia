# Sekolah Bekasi CIA

Education-first workspace for school selection and family financial planning.

## What is included

- Agent setup
	- Custom planning agent: `.github/agents/claude-education-planner.agent.md`
	- Workspace agent guide: `.github/AGENTS.md`
	- Root shortcut list: `AGENTS.md`

- Preschool decision artifacts (TK-A and TK-B)
	- Comparison matrix template: `planning/preschool_comparison_matrix_template.csv`
	- Rating rubric and weighting rules: `planning/preschool_rating_rubric.md`
	- Scenario draft from current budget baseline: `planning/financial_scenarios.md`
	- Extracted candidate dataset from brochure images: `planning/preschool_candidates_extracted_provisional.csv`
	- Updated final ranking notes: `planning/preschool_preliminary_ranking.md`

- Organized structure for latest run
	- Raw brochure image inputs: `data/inputs/preschool/brochure_images/2026-04-18_whatsapp/`
	- Home base and decision rules: `data/context/home_base_and_rules.md`
	- Methodology details: `analysis/preschool/ranking_methodology_2026.md`
	- Cost component calculation report: `analysis/preschool/cost_component_calculation_report_2026.md`
	- Comprehensive school audit report: `analysis/preschool/comprehensive_school_cost_audit_2026-04-19.md`
	- Final output index: `outputs/README.md`
	- CSV outputs: `outputs/tables/`
	- Excel-openable workbook outputs: `outputs/workbooks/`

- Budget dashboard
	- Google Sheets and Looker export pipeline: `dashboard/export_for_looker.py`
	- Google Sheets and Looker setup: `dashboard/GOOGLE_SHEETS_LOOKER_SETUP.md`
	- Optional Streamlit app: `dashboard/app.py`
	- Dashboard usage guide: `dashboard/README.md`

## Quick start (Google Sheets and Looker)

1. Install dependencies
	 - `pip install -r requirements.txt`
2. Rebuild school ranking tables from extracted candidate inputs
	- `python analysis/preschool/rebuild_rankings.py --write-candidates`
3. Export normalized tables
	- `python dashboard/export_for_looker.py --input "Pengeluaran_budget_template (1).xlsx" --output dashboard/exports`

Optional local app:
- `streamlit run dashboard/app.py`

## Current preschool scoring model

- Curriculum: 35%
- Languages: 20%
- Cost efficiency: 35%
- Continuity bonus to Elementary: tracked as a note only (currently excluded from scoring)

This model is designed to balance education excellence and financial sustainability.
