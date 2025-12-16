from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
FIG_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"

for d in [DATA_DIR, OUTPUT_DIR, FIG_DIR, TABLE_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# File locations
DATAMX_JSON = DATA_DIR / "datamx_climate.json"

# Plot settings
FIG_DPI = 140
STYLE = "ggplot"
RANDOM_STATE = 42
