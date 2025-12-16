from src.eda import plot_national_timeseries
from src.clustering import run_kmeans
from src.anomalies import plot_anomalies
from src.chaos import lle_national_temperature
from src.data_io import load_datamx_json
from src.derivatives import example_pricing

def main():
    print("Running Climate–Chaos–Clustering pipeline...\n")
    print("1️⃣ EDA ...")
    print(plot_national_timeseries())

    print("2️⃣ KMeans clustering ...")
    print(run_kmeans())

    print("3️⃣ Anomalies (Ciudad de México) ...")
    plot_anomalies("Ciudad de México")

    print("4️⃣ Chaos analysis ...")
    lle = lle_national_temperature()
    print("LLE:", lle)

    print("5️⃣ Climate derivative example ...")
    df = load_datamx_json()
    df_state = df[df["ENTIDAD"]=="Ciudad de México"]
    print(example_pricing(df_state))

if __name__ == "__main__":
    main()
