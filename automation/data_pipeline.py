
import pandas as pd
import numpy as np

product_mapping = {
    "Wireless Earbuds": "P1001",
    "Smart Watch": "P1002",
    "Bluetooth Speaker": "P1003",
    "Running Shoes": "P2001",
    "Cotton T-Shirt": "P2002",
    "Backpack": "P2003",
    "Mixer Grinder": "P3001",
    "Water Bottle": "P3002",
    "Bedsheet Set": "P3003",
    "Face Serum": "P4001",
    "Sunscreen SPF 50": "P4002",
    "Yoga Mat": "P5001",
    "Cricket Bat": "P5002",
    "Data Analytics Handbook": "P6001",
    "Python Programming": "P6002"
}

def clean_events(df):
    df = df.drop_duplicates().copy()

    df["event_timestamp"] = pd.to_datetime(
        df["event_timestamp"], errors="coerce"
    )

    df["event_name"] = (
        df["event_name"].astype("string").str.strip().str.lower()
    )

    df["city"] = df["city"].astype("string").str.strip()
    df["product_name"] = df["product_name"].astype("string").str.strip()

    missing_id = df["product_id"].isna()

    df.loc[missing_id, "product_id"] = (
        df.loc[missing_id, "product_name"].map(product_mapping)
    )

    return df


def clean_orders(df):
    df = df.drop_duplicates().copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"], errors="coerce"
    )

    df["city"] = df["city"].astype("string").str.strip()
    df["product_name"] = df["product_name"].astype("string").str.strip()

    gross = pd.to_numeric(df["gross_amount_inr"], errors="coerce")
    net = pd.to_numeric(df["net_amount_inr"], errors="coerce")

    calculated_discount = ((gross - net) / gross * 100).where(
        gross > 0
    )

    df["discount_pct_clean"] = (
        pd.to_numeric(df["discount_pct"], errors="coerce")
        .fillna(calculated_discount)
        .round(2)
    )

    return df
