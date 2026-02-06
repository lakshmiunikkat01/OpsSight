import pandas as pd

def load_excel(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    print("RAW COLUMNS FROM EXCEL:")
    print(df.columns.tolist())
    return df
