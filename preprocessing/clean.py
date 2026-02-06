import pandas as pd

CORE_COLUMNS = [
    "region",
    "department",
    "sector",
    "year",
    "full yr",
    "cost split",
    "divisor"
]

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[[c for c in df.columns if c in CORE_COLUMNS]].copy()

    for col in ["full yr", "cost split", "divisor"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    required = [c for c in ["cost split", "divisor"] if c in df.columns]

    if not required:
        return df

    df = df.dropna(subset=required, how="any")
    return df

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "cost split" in df.columns and "divisor" in df.columns:
        df["ops_value"] = df["cost split"] * df["divisor"]

        if "full yr" in df.columns:
            df["ops_delta"] = df["ops_value"] - df["full yr"]

    return df
