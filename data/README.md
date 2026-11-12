Inputs, processed data, and simulation results for the Mercer St merge study. See the main README for the study design and results.
# Data files

| File | What it is | Source | Data date | Captured |
|---|---|---|---|---|
| CS11449-upstream-AADT_2026-11-04.png | Upstream NB I-5 AADT, two-way (192,010) | WSDOT traffic count system, location CS11449 | 2025 | 11/4/2026 |
| CS01700-downstream-AADT_2026-11-04.png | Downstream NB I-5 AADT, two-way (215,791) | WSDOT traffic count system, location CS01700 | 2025 | 11/4/2026 |
| CS10905_ramp_count.xlsx | NB entry ramp volume, 15-minute intervals for 24 hours (PM peak hour 836 veh/h) | WSDOT volume count report, location CS10905 | Wednesday 2/12/2025 | 11/8/2026 |
| Design-Hour-Report-2025.xlsx | K and D factors (site S212), top-200-hour volumes | WSDOT 2025 Design Hour Report | 2025 | 11/4/2026 |
| mercer_street_excel.xlsx | Geometry sheet (QGIS-traced lengths alongside Vissim drawn lengths for the baseline and alternatives) and Traffic Inputs sheet | My calculations from the sources above and the Vissim models | | |
| mercer_speed_profile_2015.csv | Average Tue-Thu speed by time of day (5-minute steps), averaged over three northbound I-5 stations at MP 167.04, 167.32, and 167.56, plus the 10th-percentile speed on slow days. Includes imputed values | UW freeway loop detector speed dataset, Zenodo record 3258904 | 2015 | 11/8/2026 |
| discover.py | Script that builds the CSV from the original dataset | The code I used | | |
| Baseline_Data_Gradual_Taper_Summary_Fixed.xlsx | Baseline scenario: raw Vissim data collection export (Baseline_Raw) and per-seed summary (Baseline_Summary) | Vissim 2027 data collection results, my summary formulas | Simulated | 11/12/2026 |
| Alt1_Data.xlsx | Alt 1 (merge +227 ft, lane-change distance 656 ft): raw export and per-seed summary | Vissim 2027 data collection results, my summary formulas | Simulated | 11/12/2026 |
| Alt1b_Data.xlsx | Alt 1b (merge +227 ft, lane-change distance 883 ft): raw export and per-seed summary | Vissim 2027 data collection results, my summary formulas | Simulated | 11/12/2026 |
| Alt1c_Data.xlsx | Alt 1c (merge +227 ft, lane-change distance 1,132 ft): raw export and per-seed summary | Vissim 2027 data collection results, my summary formulas | Simulated | 11/12/2026 |
| Mercer_Combined_Results.xlsx | Per-seed values for all four scenarios, paired differences, 95% confidence intervals, p-values, and the removals check | Copied from the four scenario workbooks above | Simulated | 11/12/2026 |

## Speed data notes

- The source dataset is about 274 MB and not included because of its size
- Speed data can be downloaded from https://zenodo.org/record/3258904. Place the file next to discover.py to reproduce the CSV
- Station prefix "i" is the increasing milepost direction, per the dataset's GitHub documentation (https://github.com/zhiyongc/Seattle-Loop-Data). I-5 mileposts increase northbound, so "i" stations are northbound
- Speeds are averages across all main lanes at each station, for Tuesday to Thursday only, for 2015, at three stations (MP 167.04, 167.32, 167.56). The dataset includes imputed values
- PM-peak averages at these stations are roughly 18 to 27 mph, with 10th-percentile speeds of roughly 6 to 14 mph.
- This is used only as a reasonableness check on modeled speeds, not for calibration. It is from a different year than the volume data, so the two are not the same period
- Citation: Yinhai Wang, Xuegang (Jeff) Ban, Zhiyong Cui, & Meixin Zhu. (2019). Freeway Inductive Loop Detector Dataset for Network-wide Traffic Speed Prediction (Version V2) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.3258904

## Simulation results notes

- Simulation results: see results/ (per-scenario Excel workbooks and a combined workbook with the paired statistics)
