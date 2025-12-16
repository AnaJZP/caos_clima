import numpy as np
import pandas as pd
from .config import TABLE_DIR

def build_weather_index(df, kind="CDD", base_temp=18.0):
    t = df["MEDIA"]
    if kind.upper()=="CDD":
        return (t - base_temp).clip(lower=0)
    else:
        return (base_temp - t).clip(lower=0)

def simulate_option_payoff(index, strike, notional=1.0):
    return notional * (index - strike).clip(lower=0)

def example_pricing(df_state, kind="CDD", base_temp=18.0, strike=None, notional=1000.0):
    idx = build_weather_index(df_state, kind, base_temp)
    if strike is None:
        strike = idx.quantile(0.7)
    payoff = simulate_option_payoff(idx, strike, notional)
    res = pd.DataFrame({"PERIODO": df_state["PERIODO"], "index": idx, "payoff": payoff})
    path = TABLE_DIR / f"weather_option_{kind.lower()}.csv"
    res.to_csv(path, index=False)
    return {"strike": float(strike), "mean_payoff": float(payoff.mean())}
