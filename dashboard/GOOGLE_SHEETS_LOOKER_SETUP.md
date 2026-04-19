# Google Sheets + Looker Studio Setup

This setup is designed for your preferred flow:
- Budget workbook mirrored in Google Drive
- Dashboard in Looker Studio
- School comparison integrated in the same reporting stack

## 1) Export workbook tables to CSV
Run from the repository root:

1. Install dependencies
- pip install -r requirements.txt

2. Export data tables
- python dashboard/export_for_looker.py --input "Pengeluaran_budget_template (1).xlsx" --output dashboard/exports

Generated files:
- dashboard/exports/monthly_summary.csv
- dashboard/exports/transactions.csv
- dashboard/exports/budget_categories.csv
- dashboard/exports/school_candidates.csv (if source file exists)

## 2) Import CSV files into Google Sheets
Create one spreadsheet and import each CSV as separate tabs:
- monthly_summary
- transactions
- budget_categories
- school_candidates

## 3) Build Looker Studio report
Create a report and add Google Sheets as the data source.

Recommended pages:
- Page 1: Household monthly performance
  - Scorecards: income, planned opex, planned savings, ending balance
  - Trend chart from monthly_summary
- Page 2: Spending behavior
  - Bar chart: budget vs actual by category
  - Table and filter: transactions by category and month
- Page 3: Preschool decision board
  - Table from school_candidates with filters
  - Highlight fields: Monthly_Opex_Effective_IDR, Two_Year_Total_IDR, Final_Score_100

## 4) Refresh workflow with Drive mirror
Whenever workbook data changes:
1. Replace workbook mirror in your Drive/local sync.
2. Run export_for_looker.py again.
3. Re-import or update sheets (depends on your chosen sync method).
4. Looker report updates from Google Sheets source.

## 5) Optional automation
If you want full auto-refresh, next step is an Apps Script trigger that:
- reads the latest uploaded workbook file
- refreshes the normalized tabs
- keeps chart schema stable in Looker Studio

I can generate that Apps Script in the next step after you share your target Google Sheet ID.
