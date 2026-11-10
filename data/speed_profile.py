# Builds mercer_speed_profile_2015.csv from the UW loop detector speed dataset.
# Download the dataset from https://zenodo.org/record/3258904 and save it as
# "speed_matrix_2015_1mph" in the same folder as this script.

import os
import re
from datetime import time
import pandas as pd

here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_pickle(os.path.join(here, "speed_matrix_2015_1mph"))
df.index = pd.to_datetime(df.index)

PREFIX = "i"                    # "i" = increasing milepost, assumed northbound
MP_MIN, MP_MAX = 167.0, 167.6   # stations near the merge

def mp(c):
    return int(re.search(r"(\d{5})$", c).group(1)) / 100

cols = [c for c in df.columns
        if c.startswith(PREFIX + "005") and MP_MIN <= mp(c) <= MP_MAX]
print("Stations used:", cols)

wk = df[df.index.day_of_week.isin([1, 2, 3])]    # Tue to Thu
avg = wk[cols].mean(axis=1)                      # average across the stations

g = avg.groupby(avg.index.time)
out = pd.DataFrame({
    "avg_speed_mph": g.mean(),
    "p10_speed_mph": g.quantile(0.10),           # slow days
}).round(1)
out.index.name = "time"

mask = [time(15, 0) <= t <= time(19, 0) for t in out.index]
print(out[mask].to_string())

out.to_csv(os.path.join(here, "mercer_speed_profile_2015.csv"))
print("Saved CSV in:", here)