import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from .features import build_climatology_features
from .config import FIG_DIR, TABLE_DIR, RANDOM_STATE
from .plot import use_style, savefig

def run_kmeans(k_min=2, k_max=6):
    use_style()
    agg = build_climatology_features()
    X = agg.drop(columns=["ENTIDAD"]).values
    Xz = StandardScaler().fit_transform(X)

    best_k, best_score, labels = None, -1, None
    for k in range(k_min, k_max+1):
        km = KMeans(n_clusters=k, random_state=RANDOM_STATE, n_init=20)
        y = km.fit_predict(Xz)
        s = silhouette_score(Xz, y)
        if s > best_score:
            best_k, best_score, labels = k, s, y

    agg["cluster"] = labels
    agg.to_csv(TABLE_DIR / "state_clusters.csv", index=False)

    fig, ax = plt.subplots(figsize=(7,5))
    sc = ax.scatter(agg["mean_temp"], agg["mean_rain"], c=agg["cluster"])
    for _, r in agg.iterrows():
        ax.text(r["mean_temp"], r["mean_rain"], r["ENTIDAD"][:5], fontsize=6)
    ax.set_title(f"KMeans Clusters (k={best_k}, silhouette={best_score:.3f})")
    ax.set_xlabel("Mean Temp (°C)"); ax.set_ylabel("Mean Rain (mm/month)")
    savefig(fig, FIG_DIR / "cluster_scatter.png")

    return {"best_k": best_k, "silhouette": best_score}
