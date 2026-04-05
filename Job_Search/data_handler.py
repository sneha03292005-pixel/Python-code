"""
data_handler.py — CSV ingestion and Pandas data cleaning / transformation
Smart Job Tracker | Sneha B
"""

import pandas as pd
from db import insert_job


# ── LOAD & CLEAN CSV ──────────────────────────────────────────────────────────

def load_and_clean_csv(filepath):
    """
    Load a CSV of job applications, clean it with Pandas,
    and return a clean DataFrame.

    Expected CSV columns:
        company, role, industry, source, applied_on, status, response
    """
    df = pd.read_csv(filepath)

    print(f"[Data] Loaded {len(df)} rows from '{filepath}'")
    print(f"[Data] Columns: {list(df.columns)}")

    # ── Step 1: Standardise column names (strip spaces, lowercase) ────────────
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # ── Step 2: Drop fully empty rows ─────────────────────────────────────────
    before = len(df)
    df.dropna(how="all", inplace=True)
    print(f"[Clean] Removed {before - len(df)} fully empty rows.")

    # ── Step 3: Remove duplicate rows ─────────────────────────────────────────
    before = len(df)
    df.drop_duplicates(inplace=True)
    print(f"[Clean] Removed {before - len(df)} duplicate rows.")

    # ── Step 4: Fill missing values with sensible defaults ───────────────────
    df["industry"]   = df["industry"].fillna("Unknown")
    df["source"]     = df["source"].fillna("Unknown")
    df["status"]     = df["status"].fillna("Applied")
    df["response"]   = df["response"].fillna("No Response")
    df["applied_on"] = df["applied_on"].fillna("Unknown")

    # ── Step 5: Standardise text — strip whitespace, title-case names ─────────
    for col in ["company", "role", "industry", "source", "status", "response"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    df["company"]  = df["company"].str.title()
    df["role"]     = df["role"].str.title()
    df["industry"] = df["industry"].str.title()
    df["source"]   = df["source"].str.title()
    df["status"]   = df["status"].str.title()

    # ── Step 6: Validate and parse dates ─────────────────────────────────────
    df["applied_on"] = pd.to_datetime(df["applied_on"], errors="coerce").dt.strftime("%Y-%m-%d")
    df["applied_on"] = df["applied_on"].fillna("Unknown")

    print(f"[Clean] Final clean dataset: {len(df)} rows.\n")
    return df


# ── IMPORT CLEAN DATA INTO DB ─────────────────────────────────────────────────

def import_csv_to_db(filepath):
    """Clean CSV and insert all rows into the SQLite database."""
    df = load_and_clean_csv(filepath)
    count = 0
    for _, row in df.iterrows():
        insert_job(
            company    = row["company"],
            role       = row["role"],
            industry   = row.get("industry", "Unknown"),
            source     = row.get("source", "Unknown"),
            applied_on = row.get("applied_on", "Unknown"),
            status     = row.get("status", "Applied"),
            response   = row.get("response", "No Response")
        )
        count += 1
    print(f"[Import] {count} records imported to database.")


# ── EXPLORATORY ANALYSIS ON DATAFRAME ─────────────────────────────────────────

def analyse_dataframe(df):
    """Run basic EDA on the cleaned DataFrame and print insights."""
    print("\n" + "="*55)
    print("  EXPLORATORY DATA ANALYSIS")
    print("="*55)

    print(f"\nTotal applications  : {len(df)}")
    print(f"Unique companies    : {df['company'].nunique()}")
    print(f"Unique roles        : {df['role'].nunique()}")

    print("\n── Status breakdown ──────────────────────────────────")
    print(df["status"].value_counts().to_string())

    print("\n── Applications by industry ──────────────────────────")
    print(df["industry"].value_counts().to_string())

    print("\n── Applications by source ────────────────────────────")
    print(df["source"].value_counts().to_string())

    # Response rate
    responded = df[df["response"] != "No Response"]
    rate = round(len(responded) / len(df) * 100, 2) if len(df) > 0 else 0
    print(f"\n── Overall callback rate : {rate}% ──────────────────")

    print("="*55 + "\n")