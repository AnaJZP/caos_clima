import numpy as np
import pandas as pd
from .data_io import load_datamx_json
from .config import TABLE_DIR

def build_climatology_features() -> pd.DataFrame:
    df = load_datamx_json()
    states = df[df["ENTIDAD"]!="Nacional"].copy()
    agg = states.groupby("ENTIDAD").agg(
        mean_temp=("MEDIA","mean"),
        sd_temp=("MEDIA","std"),
        max_temp=("MAXIMA","max"),
        min_temp=("MINIMA","min"),
        mean_rain=("PRECIPITACION","mean"),
        sd_rain=("PRECIPITACION","std"),
        rain_p95=("PRECIPITACION", lambda x: np.nanpercentile(x,95)),
        dry_freq=("PRECIPITACION", lambda x: np.mean((x.fillna(0)<=1).astype(float)))
    ).reset_index()
    agg.to_csv(TABLE_DIR / "climatology_features.csv", index=False)
    return agg
