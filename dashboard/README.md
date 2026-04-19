# Preschool Budget Dashboard

Primary workflow in this repository is now Google Sheets + Looker Studio.

This dashboard stack provides:
- Monthly KPI cards (income, planned opex, planned savings, ending balance)
- Category budget vs realization chart
- Transaction feed by category
- Preschool affordability scenarios for TK-A and TK-B

## Supported workbook structure
The app is aligned to the uploaded template:
- Monthly sheet pattern like "Maret 2026" with summary in D2-D5
- Category blocks with headers "Keterangan, Tanggal, Kredit, Debit"
- A sheet named "Budget Template" for category-level budget and realization

## Preferred workflow: Google Sheets + Looker Studio
1. Export normalized tables from workbook
   - `python dashboard/export_for_looker.py --input "Pengeluaran_budget_template (1).xlsx" --output dashboard/exports`
2. Import CSV files from `dashboard/exports` into Google Sheets tabs
3. Build Looker Studio report on top of those tabs

Detailed guide:
- `dashboard/GOOGLE_SHEETS_LOOKER_SETUP.md`

## Optional local app (Streamlit)
1. Install dependencies:
   - `pip install -r requirements.txt`
2. Start app:
   - `streamlit run dashboard/app.py`

## Data source options in app
- Upload file from your machine
- Local absolute file path
- Google Drive shared link (the app converts share link to direct download)

## Google Drive note
When you upload a mirrored workbook to Google Drive, make sure link access is enabled for file reading.

## Next integration step
After your school comparison matrix is filled, we can add a merge view so school options and monthly household affordability appear in one screen.
