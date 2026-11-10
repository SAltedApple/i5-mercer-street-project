# Data files

| File | What it is | Source | Data date | Captured |
|---|---|---|---|---|
| CS11449-upstream-AADT_2026-11-04.png | Upstream NB I-5 AADT, two-way (192,010) | WSDOT traffic count system, location CS11449 | 2025 | 11/4/2026 |
| CS01700-downstream-AADT_2026-11-04.png | Downstream NB I-5 AADT, two-way (215,791) | WSDOT traffic count system, location CS01700 | 2025 | 11/4/2026 |
| CS10905_ramp_count.xlsx | NB entry ramp volume, 15-minute intervals for 24 hours (PM peak hour 836 veh/h) | WSDOT volume count report, location CS10905 | Wednesday 2/12/2025 | 11/8/2026 |
| Design-Hour-Report-2025.xlsx | K and D factors (site S212), top-200-hour volumes | WSDOT 2025 Design Hour Report | 2025 | 11/4/2026 |
| mercer_street_excel.xlsx | Geometry and Traffic Inputs sheets | My calculations from the sources above | | |
| mercer_speed_profile_2015.csv | Average Tue-Thu speed by time of day (5-minute steps), averaged over three I-5 stations at MP 167.04, 167.32, and 167.56, plus the 10th-percentile speed on slow days | UW freeway loop detector speed dataset, Zenodo record 3258904 | 2015 | 11/8/2026 |
| discover.py | Script that builds the CSV from the original dataset | The code I used | | |

## Speed data notes

- The source dataset is about 274 MB and not included because of its size. Download it from https://zenodo.org/record/3258904 and place the file next to discover.py to reproduce the CSV.
- Station prefix "i" is the increasing milepost direction, per the dataset's GitHub documentation (https://github.com/zhiyongc/Seattle-Loop-Data). I-5 mileposts increase northbound, so "i" stations are northbound.
- Speeds are averages across all main lanes at each station, for Tuesday to Thursday only, for 2015.
- Citation: Yinhai Wang, Xuegang (Jeff) Ban, Zhiyong Cui, & Meixin Zhu. (2019). Freeway Inductive Loop Detector Dataset for Network-wide Traffic Speed Prediction (Version V2) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.3258904
