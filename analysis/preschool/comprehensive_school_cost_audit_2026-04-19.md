# Comprehensive School Cost Audit Report

Date: 2026-04-19

## Scope

This report consolidates four layers for every school in the current dataset:

1. Raw extracted data from each JPEG source
2. Normalization rule implementation used to convert raw fee formats
3. Finalized entry in the current file `planning/preschool_candidates_extracted_provisional.csv`
4. Possible links to check updated cost information

Primary sources:
- Raw images: [data/inputs/preschool/brochure_images/2026-04-18_whatsapp](data/inputs/preschool/brochure_images/2026-04-18_whatsapp)
- Current normalized table: [planning/preschool_candidates_extracted_provisional.csv](planning/preschool_candidates_extracted_provisional.csv)
- Methodology: [analysis/preschool/ranking_methodology_2026.md](analysis/preschool/ranking_methodology_2026.md)

Note:
- OCR command-line tools were not available in the environment, so raw extraction below was performed via visual transcription from the image files.

## 1) Raw Extracted Data By JPEG

| JPEG | Type | School or Content | Raw extracted fee data |
|---|---|---|---|
| [WhatsApp Image 2026-04-18 at 17.12.56.jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.56.jpeg) | Cover | Part 2 cover | No school fee values |
| [WhatsApp Image 2026-04-18 at 17.12.57.jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.57.jpeg) | School card | Embun Pagi Islamic School | Pendaftaran 800000; Uang Pangkal 21000000; Uang Kegiatan/Tahun 7660000; SPP/Bulan 2500000 |
| [WhatsApp Image 2026-04-18 at 17.12.58.jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58.jpeg) | School card | Salsabila Islamic School | Pendaftaran 450000; Uang Pangkal 21655000; Uang Kegiatan/Tahun -; SPP/Bulan 1300000 |
| [WhatsApp Image 2026-04-18 at 17.12.58 (1).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(1).jpeg) | School card | Nassa School | Pendaftaran 750000; Uang Pangkal 24388000; Uang Kegiatan/Tahun -; SPP 21431000 per tahun |
| [WhatsApp Image 2026-04-18 at 17.12.58 (2).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(2).jpeg) | School card | Little Key | Pendaftaran 300000; Uang Pangkal 12000000; Uang Kegiatan/Tahun 3800000; SPP/Bulan 1380000 |
| [WhatsApp Image 2026-04-18 at 17.12.58 (3).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(3).jpeg) | School card | Madina Islamic School Galaxy | Pendaftaran -; Uang Pangkal 15800000; Uang Kegiatan/Tahun 6700000; SPP/Bulan 1750000 |
| [WhatsApp Image 2026-04-18 at 17.12.58 (4).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(4).jpeg) | School card | Unity School | Pendaftaran 400000; Uang Pangkal 18000000; Uang Kegiatan/Tahun 2200000; SPP/Bulan 1700000 |
| [WhatsApp Image 2026-04-18 at 17.12.58 (5).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(5).jpeg) | School card | Global Prestasi School | Pendaftaran 600000; Uang Pangkal 39000000; Uang Kegiatan/Tahun -; SPP 11700000 per quarter (3 bulan) |
| [WhatsApp Image 2026-04-18 at 17.12.58 (6).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(6).jpeg) | Context | Clarification slide | No school fee values |
| [WhatsApp Image 2026-04-18 at 17.12.58 (7).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(7).jpeg) | School card | Sekolah Victory Plus (SVP) | Pendaftaran -; Uang Pangkal 35300000 (for 2 years TK); Uang Kegiatan/Tahun -; SPP 11025000 per term (3 bulan) |
| [WhatsApp Image 2026-04-18 at 17.12.58 (8).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(8).jpeg) | School card | HighScope Bekasi | Pendaftaran -; Uang Pangkal 11500000; Uang Kegiatan/Tahun -; SPP 8450000 per term (3 bulan) |
| [WhatsApp Image 2026-04-18 at 17.12.58 (9).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(9).jpeg) | Closing | Part 2 close | No school fee values |
| [WhatsApp Image 2026-04-18 at 17.12.58 (10).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(10).jpeg) | Cover | Part 1 cover | No school fee values |
| [WhatsApp Image 2026-04-18 at 17.12.58 (11).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(11).jpeg) | School card | Kinderfield Bekasi | Pendaftaran -; Uang Pangkal 20000000; Uang Tahunan 5500000; SPP 5900000 per term (3 bulan) |
| [WhatsApp Image 2026-04-18 at 17.12.58 (12).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(12).jpeg) | School card | Almacita School | Pendaftaran 700000; Uang Pangkal 25000000; Uang Tahunan -; SPP 2000000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (13).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(13).jpeg) | School card | Kidea Bekasi Timur | Pendaftaran 350000; Uang Pangkal -; Uang Tahunan 6500000 to 7000000; SPP 1800000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (14).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(14).jpeg) | School card | Sekolah Alam Bekasi | Pendaftaran 650000; Uang Pangkal 11000000; Uang Tahunan 3900000 (visual text appears as 3.9000.000); SPP 925000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (15).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(15).jpeg) | School card | Al-Azhar 11 Kemang | Pendaftaran 600000; Uang Pangkal 28815000; Uang Tahunan 800000; SPP 2375000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (16).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(16).jpeg) | School card | Islamic Green School | Pendaftaran -; Uang Pangkal 10450000; Uang Kegiatan 5170000; SPP 990000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (17).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(17).jpeg) | School card | Akhyar IIS | Pendaftaran 550000; Uang Pangkal 21000000; Uang Kegiatan -; SPP 700000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (18).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(18).jpeg) | School card | Kiwi Kids | Pendaftaran 300000; Uang Pangkal 6770000; Uang Kegiatan 1800000; SPP 1200000 per bulan |
| [WhatsApp Image 2026-04-18 at 17.12.58 (19).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(19).jpeg) | Teaser | Part 1 teaser for Part 2 list | No school fee values |

## 2) Normalization Rule Implementation

Field mapping implemented in current CSV:
- Registration_IDR <- Pendaftaran
- One_Time_Fee_IDR <- Uang Pangkal
- Annual_Fee_IDR <- Uang Kegiatan/Tahun or Uang Tahunan
- Monthly_SPP_IDR <- SPP normalized to monthly

Normalization logic:
- If SPP is monthly: Monthly_SPP_IDR = SPP
- If SPP is term or quarter with 3 months: Monthly_SPP_IDR = SPP divided by 3
- If SPP is yearly: Monthly_SPP_IDR = SPP divided by 12
- If annual fee is shown as range: use midpoint
- If fee field is dash: value set to 0 in normalized CSV

Cost model formulas currently used:
- Monthly_Transport_IDR = Distance_OneWay_KM x 2 x 2500 x 22
- Monthly_Opex_Effective_IDR = Monthly_SPP_IDR + (Annual_Fee_IDR / 12) + Monthly_Transport_IDR
- Two_Year_Total_IDR = Registration_IDR + One_Time_Fee_IDR + (Annual_Fee_IDR x 2) + (Monthly_SPP_IDR x 24) + (Monthly_Transport_IDR x 24)

## 3) Finalized Entry Per School and Possible Updated Cost Links

### Embun Pagi Islamic School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.57.jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.57.jpeg)
- Raw extracted data: pendaftaran 800000; pangkal 21000000; kegiatan tahunan 7660000; spp bulanan 2500000
- Normalization implementation: no unit conversion needed
- Finalized current entry: Monthly_SPP 2500000; Annual_Fee 7660000; Registration 800000; One_Time 21000000; Distance 10.0; Monthly_Transport 1100000; Monthly_Opex_Effective 4238333; Two_Year_Total 123520000
- Possible updated cost links:
  - https://www.google.com/search?q=Embun+Pagi+Islamic+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Embun+Pagi+Islamic+School+Bekasi

### Salsabila Islamic School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58.jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58.jpeg)
- Raw extracted data: pendaftaran 450000; pangkal 21655000; kegiatan tahunan -; spp bulanan 1300000
- Normalization implementation: annual fee set to 0 because raw card shows dash
- Finalized current entry: Monthly_SPP 1300000; Annual_Fee 0; Registration 450000; One_Time 21655000; Distance 5.5; Monthly_Transport 605000; Monthly_Opex_Effective 1905000; Two_Year_Total 67825000
- Possible updated cost links:
  - https://www.google.com/search?q=Salsabila+Islamic+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Salsabila+Islamic+School+Bekasi

### Nassa School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (1).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(1).jpeg)
- Raw extracted data: pendaftaran 750000; pangkal 24388000; kegiatan tahunan -; spp 21431000 per tahun
- Normalization implementation: Monthly_SPP = 21431000 / 12 = 1785917
- Finalized current entry: Monthly_SPP 1785917; Annual_Fee 0; Registration 750000; One_Time 24388000; Distance 7.0; Monthly_Transport 770000; Monthly_Opex_Effective 2555917; Two_Year_Total 86480008
- Possible updated cost links:
  - https://www.google.com/search?q=Nassa+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Nassa+School+Bekasi

### Little Key
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (2).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(2).jpeg)
- Raw extracted data: pendaftaran 300000; pangkal 12000000; kegiatan tahunan 3800000; spp bulanan 1380000
- Normalization implementation: no unit conversion needed
- Finalized current entry: Monthly_SPP 1380000; Annual_Fee 3800000; Registration 300000; One_Time 12000000; Distance 11.0; Monthly_Transport 1210000; Monthly_Opex_Effective 2906667; Two_Year_Total 82060000
- Possible updated cost links:
  - https://www.google.com/search?q=Little+Key+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Little+Key+Bekasi

### Madina Islamic School Galaxy
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (3).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(3).jpeg)
- Raw extracted data: pendaftaran -; pangkal 15800000; kegiatan tahunan 6700000; spp bulanan 1750000
- Normalization implementation: registration set to 0 because raw card shows dash
- Finalized current entry: Monthly_SPP 1750000; Annual_Fee 6700000; Registration 0; One_Time 15800000; Distance 2.5; Monthly_Transport 275000; Monthly_Opex_Effective 2583333; Two_Year_Total 77800000
- Possible updated cost links:
  - https://www.google.com/search?q=Madina+Islamic+School+Galaxy+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Madina+Islamic+School+Galaxy+Bekasi

### Unity School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (4).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(4).jpeg)
- Raw extracted data: pendaftaran 400000; pangkal 18000000; kegiatan tahunan 2200000; spp bulanan 1700000
- Normalization implementation: no unit conversion needed
- Finalized current entry: Monthly_SPP 1700000; Annual_Fee 2200000; Registration 400000; One_Time 18000000; Distance 2.0; Monthly_Transport 220000; Monthly_Opex_Effective 2103333; Two_Year_Total 68880000
- Possible updated cost links:
  - https://www.google.com/search?q=Unity+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Unity+School+Bekasi

### Global Prestasi School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (5).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(5).jpeg)
- Raw extracted data: pendaftaran 600000; pangkal 39000000; kegiatan tahunan -; spp 11700000 per quarter (3 bulan)
- Normalization implementation: Monthly_SPP = 11700000 / 3 = 3900000; annual fee set to 0
- Finalized current entry: Monthly_SPP 3900000; Annual_Fee 0; Registration 600000; One_Time 39000000; Distance 4.5; Monthly_Transport 495000; Monthly_Opex_Effective 4395000; Two_Year_Total 145080000
- Possible updated cost links:
  - https://www.google.com/search?q=Global+Prestasi+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Global+Prestasi+School+Bekasi

### Sekolah Victory Plus (SVP)
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (7).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(7).jpeg)
- Raw extracted data: pendaftaran -; pangkal 35300000 for 2 years TK; kegiatan tahunan -; spp 11025000 per term (3 bulan)
- Normalization implementation: Monthly_SPP = 11025000 / 3 = 3675000; registration and annual fee set to 0
- Finalized current entry: Monthly_SPP 3675000; Annual_Fee 0; Registration 0; One_Time 35300000; Distance 7.5; Monthly_Transport 825000; Monthly_Opex_Effective 4500000; Two_Year_Total 143300000
- Possible updated cost links:
  - https://www.google.com/search?q=Sekolah+Victory+Plus+(SVP)+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Sekolah+Victory+Plus+SVP+Bekasi

### HighScope Bekasi
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (8).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(8).jpeg)
- Raw extracted data: pendaftaran -; pangkal 11500000; kegiatan tahunan -; spp 8450000 per term (3 bulan)
- Normalization implementation: Monthly_SPP = 8450000 / 3 = 2816667; registration and annual fee set to 0
- Finalized current entry: Monthly_SPP 2816667; Annual_Fee 0; Registration 0; One_Time 11500000; Distance 6.0; Monthly_Transport 660000; Monthly_Opex_Effective 3476667; Two_Year_Total 94940008
- Possible updated cost links:
  - https://www.google.com/search?q=HighScope+Bekasi+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=HighScope+Bekasi

### Kinderfield Bekasi
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (11).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(11).jpeg)
- Raw extracted data: pendaftaran -; pangkal 20000000; uang tahunan 5500000; spp 5900000 per term (3 bulan)
- Normalization implementation: Monthly_SPP = 5900000 / 3 = 1966667; registration set to 0
- Finalized current entry: Monthly_SPP 1966667; Annual_Fee 5500000; Registration 0; One_Time 20000000; Distance 9.0; Monthly_Transport 990000; Monthly_Opex_Effective 3415000; Two_Year_Total 101960008
- Possible updated cost links:
  - https://www.google.com/search?q=Kinderfield+Bekasi+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Kinderfield+Bekasi

### Almacita School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (12).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(12).jpeg)
- Raw extracted data: pendaftaran 700000; pangkal 25000000; uang tahunan -; spp bulanan 2000000
- Normalization implementation: annual fee set to 0 because raw card shows dash
- Finalized current entry: Monthly_SPP 2000000; Annual_Fee 0; Registration 700000; One_Time 25000000; Distance 8.0; Monthly_Transport 880000; Monthly_Opex_Effective 2880000; Two_Year_Total 94820000
- Possible updated cost links:
  - https://www.google.com/search?q=Almacita+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Almacita+School+Bekasi

### Kidea Bekasi Timur
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (13).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(13).jpeg)
- Raw extracted data: pendaftaran 350000; pangkal -; uang tahunan 6500000 to 7000000; spp bulanan 1800000
- Normalization implementation: Annual_Fee midpoint used = (6500000 + 7000000) / 2 = 6750000; one-time fee set to 0
- Finalized current entry: Monthly_SPP 1800000; Annual_Fee 6750000; Registration 350000; One_Time 0; Distance 3.0; Monthly_Transport 330000; Monthly_Opex_Effective 2692500; Two_Year_Total 64970000
- Possible updated cost links:
  - https://www.google.com/search?q=Kidea+Bekasi+Timur+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Kidea+Bekasi+Timur

### Sekolah Alam Bekasi
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (14).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(14).jpeg)
- Raw extracted data: pendaftaran 650000; pangkal 11000000; uang tahunan appears as 3.9000.000 and interpreted as 3900000; spp bulanan 925000
- Normalization implementation: no unit conversion needed after annual fee interpretation
- Finalized current entry: Monthly_SPP 925000; Annual_Fee 3900000; Registration 650000; One_Time 11000000; Distance 10.0; Monthly_Transport 1100000; Monthly_Opex_Effective 2350000; Two_Year_Total 68050000
- Possible updated cost links:
  - https://www.google.com/search?q=Sekolah+Alam+Bekasi+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Sekolah+Alam+Bekasi

### Al-Azhar 11 Kemang
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (15).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(15).jpeg)
- Raw extracted data: pendaftaran 600000; pangkal 28815000 (includes TK-B education, field trip, uniform); uang tahunan 800000; spp bulanan 2375000
- Normalization implementation: no unit conversion needed
- Finalized current entry: Monthly_SPP 2375000; Annual_Fee 800000; Registration 600000; One_Time 28815000; Distance 7.5; Monthly_Transport 825000; Monthly_Opex_Effective 3266667; Two_Year_Total 107815000
- Possible updated cost links:
  - https://www.google.com/search?q=Al-Azhar+11+Kemang+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Al-Azhar+11+Kemang+Bekasi

### Islamic Green School
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (16).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(16).jpeg)
- Raw extracted data: pendaftaran -; pangkal 10450000; uang kegiatan 5170000; spp bulanan 990000
- Normalization implementation: annual fee interpreted from uang kegiatan and set to 5170000; registration set to 0
- Finalized current entry: Monthly_SPP 990000; Annual_Fee 5170000; Registration 0; One_Time 10450000; Distance 15.0; Monthly_Transport 1650000; Monthly_Opex_Effective 3070833; Two_Year_Total 84150000
- Possible updated cost links:
  - https://www.google.com/search?q=Islamic+Green+School+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Islamic+Green+School+Bekasi

### Akhyar IIS
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (17).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(17).jpeg)
- Raw extracted data: pendaftaran 550000; pangkal 21000000; uang kegiatan -; spp bulanan 700000
- Normalization implementation: annual fee set to 0 because raw card shows dash
- Finalized current entry: Monthly_SPP 700000; Annual_Fee 0; Registration 550000; One_Time 21000000; Distance 4.0; Monthly_Transport 440000; Monthly_Opex_Effective 1140000; Two_Year_Total 48910000
- Possible updated cost links:
  - https://www.google.com/search?q=Akhyar+IIS+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Akhyar+IIS+Bekasi

### Kiwi Kids
- Source JPEG: [WhatsApp Image 2026-04-18 at 17.12.58 (18).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(18).jpeg)
- Raw extracted data: pendaftaran 300000; pangkal 6770000; uang kegiatan 1800000; spp bulanan 1200000
- Normalization implementation: no unit conversion needed
- Finalized current entry: Monthly_SPP 1200000; Annual_Fee 1800000; Registration 300000; One_Time 6770000; Distance 1.5; Monthly_Transport 165000; Monthly_Opex_Effective 1515000; Two_Year_Total 43430000
- Possible updated cost links:
  - https://www.google.com/search?q=Kiwi+Kids+Bekasi+biaya+TK
  - https://www.google.com/maps/search/?api=1&query=Kiwi+Kids+Bekasi

## 4) Data Quality and Recheck Flags

- Kidea Bekasi Timur: annual fee is a range; midpoint assumption currently used.
- Sekolah Alam Bekasi: annual fee text appears with a formatting typo in image; interpreted as 3900000.
- SVP: one-time fee explicitly states for 2 years TK, and is currently treated as one-time fee in the 2-year model.
- Slides [WhatsApp Image 2026-04-18 at 17.12.58 (6).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(6).jpeg), [WhatsApp Image 2026-04-18 at 17.12.58 (9).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(9).jpeg), [WhatsApp Image 2026-04-18 at 17.12.58 (10).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(10).jpeg), and [WhatsApp Image 2026-04-18 at 17.12.58 (19).jpeg](data/inputs/preschool/brochure_images/2026-04-18_whatsapp/WhatsApp%20Image%202026-04-18%20at%2017.12.58%20(19).jpeg) are context/cover slides and contain no direct fee values.

## 5) Ready For Next Step

This report can be used as the baseline checklist for scraping and updating latest fees. The next update pass should validate:
- Effective academic year of each fee
- Whether annual/activity fees are mandatory or optional
- Whether SPP units changed (monthly versus term versus yearly)
- Which items are included inside one-time fee packages
