# Data Inputs

This folder stores raw and semi-processed input artifacts used to build planning datasets.

## Structure

- `preschool/brochure_images/`
  - Raw brochure snapshots grouped by collection batch date/source.
  - Current batch: `preschool/brochure_images/2026-04-18_whatsapp/`

## Naming Rules

- Keep original filenames for traceability to source captures.
- Create a new dated subfolder for each intake batch.
- Avoid storing raw image files at repository root.

## Usage Notes

- `planning/preschool_candidates_extracted_provisional.csv` is the extracted table built from these raw brochure images.
- Ranking outputs in `outputs/tables/` are downstream artifacts and should not be edited manually.