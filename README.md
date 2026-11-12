# I-5 / Mercer St. On-Ramp Merge Analysis

This project looks into whether lengthening the Mercer Street on-ramp merge onto northbound I-5 would reduce congestion and delay during the weekday PM peak. The Mercer interchange sits between downtown Seattle, South Lake Union and Capitol Hill, which may provide traffic that disrupts the flow of mainline northbound I-5. Using WSDOT traffic count data for a busy weekday PM peak, I built a Vissim microsimulation of the ramp and a stretch of I-5 before and after the merge. Because of the limits of the Vissim student license, each run simulates only a 10 minute window. Ramp geometry was measured in QGIS. I compared the existing layout against a merge lane lengthened by about 227 ft (+19.9%), using downstream speed, vehicle counts, and queue delay, with ten random seeds per scenario. The longer merge lane did not improve downstream speed under the modeled conditions (see Results). This project is an independent conceptual analysis and doesn't account for right of way, cost, or construction constraints.

## Status

Complete. Geometry, traffic inputs, Vissim modeling, analysis, and documentation are finished. Results are below..

## Data sources

- Upstream NB I-5 AADT: WSDOT location CS11449, 2025, two-way (192,010)
- Downstream NB I-5 AADT: WSDOT location CS01700, 2025, two-way (215,791)
- NB entry ramp count: WSDOT location CS10905 (SR 5 ramp Q116735, after the Q116726R off-ramp, NB branch after both express-lane exits). 24-hour video count on Wednesday 2/12/2025, 15-minute intervals, accepted by WSDOT QC. PM peak hour 16:00 to 17:00 = 836 veh/h. File: data/CS10905_ramp_count.xlsx
- K-factor (0.066) and D-factor (0.5329): site S212 (SR 5, MP 162.35, Seattle), WSDOT 2025 Design Hour Report, 30th highest hour
- Capacity: Highway Capacity Manual, 7th Edition, basic freeway segment, 60 mph free-flow speed, 2,300 pc/h/ln
- Ramp geometry: measured in QGIS on Esri World Imagery (satellite) and traced into a GeoPackage. The merge lane measures 1,131.8 ft from the start of the gore point to the end of the taper. The Vissim baseline totals 1,147 ft (link 1 at 857 ft plus connector 10002 at 290 ft), about 1.3% longer, reflecting tracing precision and how the gradual taper is built in Vissim.
- Speed reference: UW freeway loop detector dataset (Zenodo, 2015, CC BY 4.0), 5-minute speeds, Tuesday to Thursday, averaged over northbound I-5 stations near MP 167.0 to 167.6 (script: [discover.py], output: [mercer_speed_profile_2015.csv] in data/). Includes imputed values. Used only as a reasonableness check, not for calibration. Citation: Wang, Ban, Cui & Zhu (2019), Freeway Inductive Loop Detector Dataset for Network-wide Traffic Speed Prediction (Version V2) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.3258904
- Vehicle mix: 89.5% cars, 5.5% heavy goods vehicles (single-unit 2.9% + combination 2.6%, from the WSDOT Design Hour Report Western Washington urban major route group average, because S212 has no truck data), and 5% light goods vehicles (Vissim default, an assumption)
- Simulation results: per-scenario Excel workbooks with raw Vissim exports and per-seed summaries, plus a combined workbook with the paired statistics (see Files)

## Assumptions

- AADT values are two-way. Peak hour northbound volume is estimated with AADT x K x D
- Mainline volume is an estimate from AADT, not a measured hourly volume at Mercer
- Upstream and downstream I-5 stretches are about 500 ft each (modeling choice, drawn lengths). Upstream is 500.2 ft in every scenario. Downstream is 500.0 ft in the baseline and 473 ft in the alternatives
- The mainline stretch beside the merge lane is assumed equal to the merge lane length
- The ramp count and the mainline estimate are treated as the same peak period
- An exit lane begins 268 ft along the downstream link in the baseline and 41 ft along it in the alternatives (the extended merge moves the exit start closer to the end of the merge). It is not modeled in any scenario, so no vehicles diverge there. The downstream measurement point is before the exit start in the baseline and after it in the alternatives
- One demand level only: 6,753 veh/h mainline and 836 veh/h ramp (about 7,589 veh/h total). A basic-segment capacity check puts this at about 82% of 9,200 pc/h (4 lanes x 2,300), but a merge breaks down earlier than a basic segment
- Freeway desired speeds are uniform 55 to 70 mph (60 mph speed limit). Ramp vehicles start at 23 to 28 mph (a guess based on a 25 mph advisory on the ramp curves) and a Desired Speed Decision 27.865 ft along the ramp switches them to the freeway distribution. They reach about 60 mph before the merge
- Driving behavior is a custom "freeway merge" set (copy of Freeway): Wiedemann 99, free lane selection, cooperative lane change on, advanced merging on, 60 s waiting time before diffusion. A vehicle route was added so vehicles do not disappear at the merge
- Lane-change distance (a Vissim connector setting on connector 10002, not a physical length) is 656 ft (Vissim default) in the baseline and Alt 1, 883 ft in Alt 1b (656 + 227), and 1,132 ft in Alt 1c (about the QGIS merge length). These are sensitivity settings, not calibrated values
- The merge is modeled as link 1 plus connector 10002 (gradual taper, on the inside of a left bend of I-5). An earlier sharp-taper version is superseded and not reported
- The alternatives lengthen link 1 by 227 ft. The modeled merge grows from 1,147 ft to about 1,376 ft (+19.9%; the plan targeted +20%)

## Scenarios and method

| Scenario | Link 1 | Merge extension | Lane-change distance |
|---|---:|---:|---:|
| Baseline | 857 ft | none | 656 ft |
| Alt 1 | 1,084 ft | +227 ft | 656 ft |
| Alt 1b | 1,084 ft | +227 ft | 883 ft |
| Alt 1c | 1,084 ft | +227 ft | 1,132 ft |

- 600 s runs, 10 seeds (42 to 51), the same seeds in every scenario. The first 2 minutes (network filling) are excluded, so the analysis window is 120 to 600 s
- Measured at three data collection points (upstream mainline, ramp, downstream before the exit) in 60 s intervals
- Downstream speed per run = sum(vehicles x 1-min mean speed) / sum(vehicles) over the eight 1-min intervals from 120 to 600 s. The scenario figure is the mean of the ten per-run values
- The downstream measurement point is 60 ft along link 2 in the baseline and 59 ft along it in the alternatives, so it sits at the same distance (within 1 ft) past the end of the merge in every scenario. The exit lane begins 268 ft along link 2 in the baseline and 41 ft along it in the alternatives, so the point is before the exit start in the baseline and 18 ft past it in the alternatives. Since the exit is not modeled, no vehicles diverge there and the vehicles counted are unaffected. An earlier Alt 1 export with the point in a different position gave a larger slowdown (about 6.9 mph), so the slowdown is not an artifact of detector placement
- Scenarios are compared seed by seed. Each 95% confidence interval is mean difference +/- t(0.975, df = 9) x SD(differences) / sqrt(10), and p-values are from a paired t-test
- Alt 1 vs the baseline isolates the geometry change, since both use 656 ft. Alt 1b and Alt 1c vs Alt 1 isolate the lane-change distance on the extended lane. Alt 1b and Alt 1c vs the baseline change both at once, because the baseline was only run at 656 ft

## Limitations

- Observed speeds are from 2015 and are not from the same period as the volume data, so the model is checked for reasonableness only and is not calibrated
- The ramp volume comes from a single weekday count (Wednesday 2/12/2025)
- The speed reference is 2015 loop detector data, averaged across all lanes at stations near MP 167.0 to 167.6, and includes imputed values. It shows PM-peak speeds of about 20 to 30 mph, far below the modeled 52 to 60 mph. That is expected given the short empty-start runs and no downstream bottleneck, and it is not a calibration target
- The mainline estimate uses a busy-hour factor from a different location (S212)
- Each run is limited to 10 minutes (600 s) by the Vissim student license and starts from an empty network, so it cannot reproduce a full PM peak or developed congestion
- Basemap imagery is not included in the QGIS project and loads from the internet
- The ramp volume comes from a single weekday count (Wednesday 2/12/2025)
- No downstream bottleneck or exit traffic is modeled, so real queues that spill back through Mercer St are absent
- Ramp acceleration is idealized. Ramp vehicles reach freeway speed before the merge, so a longer merge lane has little acceleration benefit to offer in this model
- Results depend on the lane-change distance. The baseline was only run at 656 ft, so Alt 1b and Alt 1c differ from it in two ways (geometry and lane-change distance)
- Confidence intervals cover random-seed variation only, not modeling assumptions
- Vissim does not represent curve-related driver behavior
- Travel-time and queue-counter measurements were not analyzed
- These are conceptual findings under stated assumptions. They are not a prediction of real-world change at Mercer St
- The extended merge ends close to where the exit lane begins (41 ft into the downstream link vs 268 ft in the baseline). Because the exit is not modeled, any interaction between the merge and diverging exit traffic is not captured, and the downstream measurement point lies past the exit start in the alternatives

## Tools

QGIS, Microsoft Excel, PTV Vissim (Student) 2027, Python (pandas)

## Files

- qgis/: QGIS project and traced geometry (keep the .qgz and .gpkg in the same folder)
- data/: traffic inputs spreadsheet, saved WSDOT data, speed reference CSV, and simulation results (see data/README.md)
- [data/Baseline_Data_Gradual_Taper_Summary_Fixed.xlsx, Alt1_Data.xlsx, Alt1b_Data.xlsx, Alt1c_Data.xlsx]: raw Vissim exports and per-seed summaries for each scenario
- [data/Mercer_Combined_Results.xlsx]: per-seed values, paired differences, confidence intervals, and removals check for all four scenarios
- [discover.py]: builds the 2015 speed profile CSV from the Zenodo dataset

Not uploaded: Python virtual environment, Vissim working/layout/error/result files, and the 274 MB raw speed dataset.

## Results

Under the modeled demand, extending the merge lane by about 227 ft (+19.9%) did not improve downstream speed. All three extended-lane scenarios were slower than the baseline in 10 of 10 paired seeds.

| Scenario | Lane-change distance | Downstream speed, mean +/- SD (mph) | Lowest 1-min downstream speed, mean (mph) |
|---|---:|---:|---:|
| Baseline | 656 ft | 57.4 +/- 1.1 | 54.7 |
| Alt 1 | 656 ft | 51.6 +/- 0.9 | 49.8 |
| Alt 1b | 883 ft | 52.4 +/- 0.8 | 50.1 |
| Alt 1c | 1,132 ft | 52.8 +/- 0.6 | 50.8 |

n = 10 seeds per scenario, analysis window 120 to 600 s.

Paired differences by seed (second scenario minus first), 95% confidence intervals:

| Comparison | What it isolates | Mean difference (mph) | 95% CI | p |
|---|---|---:|---|---|
| Alt 1 - Baseline | geometry only | -5.86 | -6.61 to -5.11 | < 0.001 |
| Alt 1b - Baseline | geometry + lane-change distance | -5.08 | -5.62 to -4.55 | < 0.001 |
| Alt 1c - Baseline | geometry + lane-change distance | -4.68 | -5.28 to -4.07 | < 0.001 |
| Alt 1b - Alt 1 | lane-change distance | +0.77 | +0.28 to +1.27 | 0.006 |
| Alt 1c - Alt 1 | lane-change distance | +1.18 | +0.76 to +1.61 | < 0.001 |
| Alt 1c - Alt 1b | lane-change distance | +0.41 | +0.09 to +0.73 | 0.017 |

- Increasing the lane-change distance on the extended lane recovered part of the loss, with diminishing returns, but speeds stayed about 4.7 mph or more below the baseline
- Mainline and ramp counts and speeds were identical across scenarios by design (mainline about 60.1 mph, ramp about 60.2 to 60.3 mph)
- Downstream vehicle counts were not meaningfully different from the baseline (means: 1,028.6 baseline, 1,032.4 Alt 1, 1,033.3 Alt 1b, 1,033.3 Alt 1c over 8 minutes). The difference is in speed, not in vehicles served
- Queue delay at the downstream measurement was negligible in all scenarios (mean of the per-run maximum 1-min value: 1.2 s baseline, 1.0 s Alt 1, 0.05 s Alt 1b, 0.01 s Alt 1c)
- No vehicles were removed by diffusion in any of the 40 runs (the Vissim Messages window was empty after every run)
- The confidence intervals reflect random-seed variation only

### Where the slowdown occurs (seed 42)
In the extended scenarios, lane 5 clears earlier, the adjacent through lane (lane 4) slows approaching the taper, and the slowing spreads into lanes 1 to 3 with partial recovery farther downstream. This fits a local merging disturbance, but the cause is not established. Possible explanations are the position and timing of lane changes, how mandatory and cooperative lane changing interact, how Vissim handles the tapered connector, and the taper sitting farther into the curve. These are hypotheses, not findings.

## Conclusion

In this model, a longer merge lane did not reduce downstream delay at the tested demand, and the result depends on the lane-change distance setting. The model runs 10 minutes from an empty network with no downstream bottleneck, so it does not reproduce observed PM-peak congestion. It shows how a longer merge behaves under these assumptions and is not evidence about the real interchange.
