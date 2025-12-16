import matplotlib.pyplot as plt
from .data_io import load_datamx_json
from .config import FIG_DIR, TABLE_DIR
from .plot import use_style, savefig

def compute_anomalies(state_name: str):
    df = load_datamx_json()
    s = df[df["ENTIDAD"]==state_name].sort_values("PERIODO")
    s["month"] = s["PERIODO"].dt.month
    clim = s.groupby("month").agg(
        clim_temp=("MEDIA","mean"),
        clim_rain=("PRECIPITACION","mean")
    ).reset_index()
    s = s.merge(clim, on="month", how="left")
    s["temp_anom"] = s["MEDIA"] - s["clim_temp"]
    s["rain_anom"] = s["PRECIPITACION"] - s["clim_rain"]
    s.to_csv(TABLE_DIR / f"anomalies_{state_name}.csv", index=False)
    return s

def plot_anomalies(state_name: str):
    use_style()
    s = compute_anomalies(state_name)

    fig, ax = plt.subplots(figsize=(9,3.6))
    ax.plot(s["PERIODO"], s["temp_anom"])
    ax.set_title(f"Temperature Anomalies — {state_name}")
    ax.set_xlabel("Date"); ax.set_ylabel("°C anomaly")
    savefig(fig, FIG_DIR / f"temp_anomalies_{state_name}.png")

    fig, ax = plt.subplots(figsize=(9,3.6))
    ax.plot(s["PERIODO"], s["rain_anom"])
    ax.set_title(f"Rainfall Anomalies — {state_name}")
    ax.set_xlabel("Date"); ax.set_ylabel("mm anomaly")
    savefig(fig, FIG_DIR / f"rain_anomalies_{state_name}.png")
