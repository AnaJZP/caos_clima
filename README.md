# Climate–Chaos–Clustering (Mexico)

Nonlinear analysis of Mexican climatological data (temperature & precipitation) with:
- **EDA** of national series
- **Per–state climatology features**
- **K-Means clustering** of climate regimes
- **Monthly anomalies** (temp & rainfall)
- **Chaos indicator** (Rosenstein-style Largest Lyapunov Exponent)
- **Toy climate derivative** (degree-day index + option payoff)

Ready for research, teaching, or prototyping climate-linked hedging ideas.

---

## 📁 Project Structure

```
climate_chaos_project/
│
├── main.py
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── config.py
│   ├── plot.py
│   ├── data_io.py
│   ├── eda.py
│   ├── features.py
│   ├── clustering.py
│   ├── anomalies.py
│   ├── chaos.py
│   └── derivatives.py
│
├── data/
│   └── datamx_climate.json   # <- place your Datamx JSON here
│
└── outputs/
    ├── figures/
    └── tables/
```

---

## 🧾 Data

- **Datamx JSON** (1985–2025) with fields: `PERIODO`, `ENTIDAD`, `MINIMA`, `MEDIA`, `MAXIMA`, `PRECIPITACION`.
- Optionally enrich with INEGI/CONAGUA station metadata (lat/long/alt).

> Copy your file to: `data/datamx_climate.json`

---

## 🛠️ Setup

### 1) Create & activate virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2) Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Run the pipeline
```bash
python main.py --state "Ciudad de México"
# or another state:
python main.py --state "Jalisco"
```

---

## 📈 What it does

1. **EDA**: plots national mean temperature & precipitation time series.
2. **Features**: builds per-state climatology (means, std, extremes, dryness).
3. **Clustering**: selects K with silhouette (2..6) and plots cluster scatter.
4. **Anomalies**: monthly anomalies by state (baseline by calendar month).
5. **Chaos**: estimates LLE on national temperature (positive slope ⇒ chaos).
6. **Derivatives**: constructs a degree-day index (CDD/HDD) and a toy option payoff series.

Outputs saved in `outputs/figures` and `outputs/tables`.

---

## 🔬 Methods (brief)

- **K-Means + silhouette** for regime discovery.
- **Delay embedding (Takens)** and **Rosenstein LLE** for chaos indication.
- **Degree-days** (CDD/HDD) to proxy weather stress for hedging examples.

> This is a demonstrator; for publication-grade chaos tests, add correlation dimension (Grassberger–Procaccia), permutation entropy, and robust τ/m selection (mutual information / FNN).

---

## 🧩 Modules

- `src/eda.py`: national plots
- `src/features.py`: state features & CSV export
- `src/clustering.py`: KMeans, silhouette, scatter figure
- `src/anomalies.py`: anomalies + plots by state
- `src/chaos.py`: LLE estimator & figure
- `src/derivatives.py`: degree-day index & option payoff CSV
- `main.py`: orchestrates the full run

---

## 🧪 Quick sanity checks

After running:
- `outputs/figures/cluster_scatter.png` exists
- `outputs/tables/state_clusters.csv` lists each state with its `cluster`
- `outputs/tables/climatology_features.csv` has features
- `outputs/figures/lle_national_temperature.png` was created

---

## 📤 Push to GitHub

Repository target: `https://github.com/AnaJZP/caos_clima`

> Replace `YOUR_GITHUB_EMAIL` and `YOUR_GITHUB_NAME` with your values.

```bash
# From inside the project folder
git init
git config user.email "YOUR_GITHUB_EMAIL"
git config user.name "YOUR_GITHUB_NAME"

# If not already present, add remote
git remote add origin https://github.com/AnaJZP/caos_clima.git

# Stage and commit
git add .
git commit -m "Initial commit: climate-chaos-clustering pipeline"

# Push (main branch)
git branch -M main
git push -u origin main
```

If the remote already has commits, pull first (prefer rebase):
```bash
git pull --rebase origin main
git push
```

If the repo is private and you prefer HTTPS with token:
```bash
git remote set-url origin https://<GH_TOKEN>@github.com/AnaJZP/caos_clima.git
# then push as usual
git push -u origin main
```

---

## ✅ License and Citation

- You may use this code for research and teaching. Please cite:
  - Lorenz (1963), Grassberger & Procaccia (1983), Rosenstein et al. (1993), Dischel (2002).

---


