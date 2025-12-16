import matplotlib.pyplot as plt
from .data_io import load_datamx_json
from .config import FIG_DIR
from .plot import use_style, savefig

def plot_national_timeseries():
    use_style()
    df = load_datamx_json()
    nat = df[df["ENTIDAD"]=="Nacional"].sort_values("PERIODO")

    fig, ax = plt.subplots(figsize=(9,4))
    ax.plot(nat["PERIODO"], nat["MEDIA"])
    ax.set_title("National Mean Temperature (°C)")
    ax.set_xlabel("Date"); ax.set_ylabel("°C")
    savefig(fig, FIG_DIR / "national_mean_temperature.png")

    fig, ax = plt.subplots(figsize=(9,4))
    ax.plot(nat["PERIODO"], nat["PRECIPITACION"])
    ax.set_title("National Precipitation (mm)")
    ax.set_xlabel("Date"); ax.set_ylabel("mm")
    savefig(fig, FIG_DIR / "national_precipitation.png")

    return {"rows": len(df), "entities": df['ENTIDAD'].nunique()}
