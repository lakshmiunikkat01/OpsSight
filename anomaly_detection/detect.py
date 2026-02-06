from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    df = df.copy()

    feature_cols = []

    if "ops_value" in df.columns:
        feature_cols.append("ops_value")
    if "ops_delta" in df.columns:
        feature_cols.append("ops_delta")

    if len(feature_cols) < 1 or len(df) < 2:
        df["is_anomaly"] = 0
        return df

    X = df[feature_cols].fillna(0)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.15,
        random_state=42
    )

    preds = model.fit_predict(X)
    df["is_anomaly"] = (preds == -1).astype(int)

    return df
