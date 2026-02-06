import pandas as pd

from ingestion.ingest import load_excel
from preprocessing.clean import normalize_columns, clean_data, add_features
from anomaly_detection.detect import detect_anomalies
from insights.narrator import generate_insight

df = load_excel("data/OpsDashV1 (1) (1).xlsx")

df = normalize_columns(df)
df = clean_data(df)
df = add_features(df)

df = detect_anomalies(df)

print("\nFINAL DATA SAMPLE:\n")
print(df.head())

df_demo = pd.concat([df] * 10, ignore_index=True)
df_demo.loc[0, "ops_value"] = df_demo["ops_value"].mean() * 5
df_demo.loc[0, "ops_delta"] = df_demo["ops_delta"].mean() * 5

df_demo = detect_anomalies(df_demo)

print("\nANOMALIES:\n")
print(df_demo[df_demo["is_anomaly"] == 1][
    ["region", "department", "sector", "ops_value", "ops_delta"]
])

print("\nINSIGHTS:\n")
anomalies = df_demo[df_demo["is_anomaly"] == 1]

if anomalies.empty:
    print("No significant anomalies detected for the current data window.")
else:
    for _, row in anomalies.iterrows():
        print("-", generate_insight(row))
