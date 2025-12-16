import numpy as np
import matplotlib.pyplot as plt
from .data_io import load_datamx_json
from .plot import use_style, savefig
from .config import FIG_DIR

def estimate_lle(series, tau=1, m=3, max_iter=25, min_separation=10):
    x = np.asarray(series, dtype=float)
    N = len(x) - (m-1)*tau
    if N <= 2*max_iter+min_separation:
        return np.nan, None, None
    Y = np.zeros((N, m))
    for i in range(m):
        Y[:, i] = x[i*tau:i*tau+N]
    nn_idx = np.zeros(N, dtype=int)
    nn_dist = np.zeros(N, dtype=float)
    for i in range(N):
        d = np.linalg.norm(Y - Y[i], axis=1)
        d[max(0, i-min_separation):min(N, i+min_separation+1)] = np.inf
        j = np.argmin(d)
        nn_idx[i] = j
        nn_dist[i] = d[j]
    ts, logs = [], []
    for k in range(1, max_iter+1):
        vals = []
        for i in range(N-k):
            j = nn_idx[i]
            if j+k < N and i+k < N and np.isfinite(nn_dist[i]) and nn_dist[i]>0:
                dist = np.linalg.norm(Y[i+k]-Y[j+k])
                if np.isfinite(dist) and dist>0:
                    vals.append(np.log(dist/nn_dist[i]))
        if vals:
            ts.append(k); logs.append(np.mean(vals))
    if len(ts)<3: return np.nan, None, None
    ts, logs = np.array(ts), np.array(logs)
    fit_upto = max(5, int(0.3*len(ts)))
    A = np.vstack([ts[:fit_upto], np.ones(fit_upto)]).T
    slope, _ = np.linalg.lstsq(A, logs[:fit_upto], rcond=None)[0]
    return slope, ts, logs

def lle_national_temperature():
    use_style()
    df = load_datamx_json()
    nat = df[df["ENTIDAD"]=="Nacional"].sort_values("PERIODO")
    slope, t, logs = estimate_lle(nat["MEDIA"].dropna().values)
    if t is not None:
        fig, ax = plt.subplots()
        ax.plot(t, logs[:len(t)])
        ax.set_title(f"LLE National Temperature (slope≈{slope:.3f})")
        ax.set_xlabel("Time step"); ax.set_ylabel("Mean log divergence")
        savefig(fig, FIG_DIR / "lle_national_temperature.png")
    return slope
