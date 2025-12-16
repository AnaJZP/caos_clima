import json
import pandas as pd
from pathlib import Path
from .config import DATAMX_JSON

def load_datamx_json(path: Path = DATAMX_JSON) -> pd.DataFrame:
    """Load Datamx JSON (fields/records) and parse dtypes."""
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    cols = [c["id"] for c in raw["fields"]]
    df = pd.DataFrame(raw["records"], columns=cols)
    df["PERIODO"] = pd.to_datetime(df["PERIODO"])
    for c in ["MINIMA","MEDIA","MAXIMA","PRECIPITACION"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df
