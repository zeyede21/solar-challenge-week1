# app/utils.py
import pandas as pd
import os

def load_data(country: str) -> pd.DataFrame:
    filepath = os.path.join("data", f"{country.lower()}_clean.csv")
    return pd.read_csv(filepath, parse_dates=["Timestamp"])

def get_country_list() -> list:
    return ["benin", "togo", "sierraleone"]

def calculate_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df[["GHI", "DNI", "DHI"]].describe().loc[["mean", "50%", "std"]].rename(index={"50%": "median"})
