# I-5 / Mercer St. On-Ramp Merge Analysis

This project looks into whether the lengthening of the Mercer Street on-ramp merging onto northbound I-5 would reduce congestion and delay during the weekday PM peak. The Mercer interchange sits between downtown Seattle, South Lake Union and Capitol Hill which may provide traffic that disrupts the flow of mainline northbound I-5. By using WSDOT traffic count data from a busy weekday weekday PM peak, I will build a microsimulation with Vissim of the ramp and a stretch of I-5 before and after the merge. Because of the limits of the Vissim student license, the model will simulate only a 10 minute window of the peak. Ramp geometry will be measured in QGIS. I will test a longer merge lane and compare the data relating to delay, travel time and queue length against the existing I-5 layout. This project is an independent conceptual analysis and doesn't account in for right of way, cost nor construction constraints.

## Status

In progress. Geometry and traffic inputs are complete. Vissim model is being built. Results are pending.

## Data sources

- Upstream NB I-5 AADT: WSDOT location CS11449, 2025, two-way (192,010)
- Downstream NB I-5 AADT: WSDOT location CS01700, 2025, two-way (215,791)
- NB entry ramp count: WSDOT location CS10905 (SR 5 ramp Q116735, after the Q116726R off-ramp, NB branch after both express-lane exits). 24-hour video count on Wednesday 2/12/2025, 15-minute intervals, accepted by WSDOT QC. PM peak hour 16:00 to 17:00 = 836 veh/h. File: data/CS10905_ramp_count.xlsx
- K-factor (0.066) and D-factor (0.5329): site S212 (SR 5, MP 162.35, Seattle), WSDOT 2025 Design Hour Report, 30th highest hour
- Capacity: Highway Capacity Manual, 7th Edition, basic freeway segment, 60 mph free-flow speed, 2,300 pc/h/ln
- Ramp geometry: measured in QGIS on Esri World Imagery (satellite) and traced into a GeoPackage. The two measurement methods used agree within about 1.3%
- Speed reference: UW freeway loop detector dataset (Zenodo, 2015), 5-minute speeds, averaged over I-5 stations near MP 167.0 to 167.6. Used only as a reasonableness check on modeled speeds. The CSV is in data/

## Assumptions

- AADT values are two-way. Peak hour northbound volume is estimated with AADT x K x D
- Mainline volume is an estimate from AADT, not a measured hourly volume at Mercer
- Upstream and downstream I-5 stretches of 500 ft each (modeling choice)
- The mainline stretch beside the merge lane is assumed equal to the merge lane length
- The ramp count and the mainline estimate are treated as the same peak period

## Limitations

- No observed speeds at Mercer, so the model will be checked for reasonableness, not calibrated
- The ramp count is from February 2025
- The mainline estimate uses a busy-hour factor from a different location (S212)
- Each run is limited to 10 minutes (600 s) by the Vissim student license
- Basemap imagery is not included in the QGIS project and loads from the internet
- The ramp volume comes from a single weekday count (Wednesday 2/12/2025)
- The speed reference is from 2015 loop detector data, averaged across all lanes at stations near MP 167.0 to 167.6 and including imputed values
- The speed reference is used to check that modeled speeds are reasonable, not to calibrate the model

## Tools

QGIS, Microsoft Excel, PTV Vissim (Student) 2027

## Files

- qgis/: QGIS project and traced geometry (keep the .qgz and .gpkg in the same folder)
- data/: traffic inputs spreadsheet and saved WSDOT data

## Results

Pending
