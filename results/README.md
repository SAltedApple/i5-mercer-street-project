# Results files

Simulation results for the Mercer St merge study. See the main README for the study design and conclusions.

| File | What it is | Captured |
|---|---|---|
| Baseline_Data_Gradual_Taper_Summary_Fixed.xlsx | Baseline: raw Vissim export (Baseline_Raw) and per-seed summary (Baseline_Summary) | 11/12/2026 |
| Alt1_Data.xlsx | Alt 1 (merge +227 ft, lane-change distance 656 ft): raw export and per-seed summary | 11/12/2026 |
| Alt1b_Data.xlsx | Alt 1b (merge +227 ft, lane-change distance 883 ft) | 11/12/2026 |
| Alt1c_Data.xlsx | Alt 1c (merge +227 ft, lane-change distance 1,132 ft) | 11/12/2026 |
| Mercer_Combined_Results.xlsx | Per-seed values for all four scenarios, paired differences, 95% confidence intervals, p-values, removals check | 11/12/2026 |

## Notes

- Each scenario workbook has two sheets: a raw sheet (Vissim "Data Collection Results" export, one row per measurement per 60 s interval) and a summary sheet (one row per seed, with mean, standard deviation, min, and max rows)
- Three data collection measurements: "1: Mainline" (upstream), "2: ramp", and "3: downstream". 8 intervals per run in the analysis window, 10 runs per scenario
- Analysis window is 120 to 600 s. The first 2 minutes (network filling) are excluded from every summary
- Seeds 42 to 51, the same in every scenario. Alt workbooks use SimRun 1 to 10 (seed = SimRun + 41). The baseline workbook uses SimRun 46 to 55 (the same seeds in the same order)
- Summary columns: mainline, ramp, and downstream vehicle counts (120 to 600 s), downstream count divided by mainline plus ramp, downstream vehicle-weighted speed, lowest 1-min downstream speed, maximum 1-min downstream queue delay, and removals
- Downstream speed = sum(vehicles x 1-min mean speed) / sum(vehicles) over the 120 to 600 s intervals, from the downstream measurement
- Paired comparisons are made seed by seed in Mercer_Combined_Results.xlsx (Paired sheet). The 95% confidence interval is mean difference +/- t(0.975, df = 9) x SD(differences) / sqrt(10)
- Directly comparable: all four scenarios (same demand, same seeds, same measurement positions past the merge end, same analysis window)
- Removals: all 40 runs had zero vehicles removed by diffusion (Vissim Messages window empty after every run)
- Downstream measurement point: 60 ft along link 2 in the baseline and 59 ft in the alternatives
- Raw files are Vissim exports with the Average / Std dev / Min / Max summary rows deleted
- Earlier versions are not included: the sharp-taper baseline (superseded), and an Alt 1 export from before the downstream point was repositioned
- Link evaluation (lane segment) and queue-counter exports are not included
