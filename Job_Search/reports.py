"""
reports.py — Generate weekly summary reports and export to CSV
Smart Job Tracker | Sneha B
"""

import pandas as pd
import os
from datetime import datetime
from db import (
    fetch_all_jobs,
    response_rate_by_industry,
    top_sources,
    weekly_stats,
    status_summary
)

REPORTS_DIR = "reports"


def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)


# ── REPORT 1: Full Application List ──────────────────────────────────────────

def report_all_applications():
    jobs = fetch_all_jobs()
    if not jobs:
        print("[Report] No data found.")
        return
    df = pd.DataFrame(jobs)
    ensure_reports_dir()
    filename = os.path.join(REPORTS_DIR, "all_applications.csv")
    df.to_csv(filename, index=False)
    print(f"[Report] All applications saved → {filename}  ({len(df)} records)")
    return df


# ── REPORT 2: Weekly Summary ──────────────────────────────────────────────────

def report_weekly_summary():
    data = weekly_stats()
    if not data:
        print("[Report] No weekly data available.")
        return
    df = pd.DataFrame(data)
    ensure_reports_dir()
    filename = os.path.join(REPORTS_DIR, "weekly_summary.csv")
    df.to_csv(filename, index=False)

    print("\n" + "="*50)
    print("  WEEKLY SUMMARY REPORT")
    print("="*50)
    print(df.to_string(index=False))
    print("="*50)
    print(f"[Report] Saved → {filename}\n")
    return df


# ── REPORT 3: Callback Rate by Industry ──────────────────────────────────────

def report_industry_callback():
    data = response_rate_by_industry()
    if not data:
        print("[Report] No industry data available.")
        return
    df = pd.DataFrame(data)
    ensure_reports_dir()
    filename = os.path.join(REPORTS_DIR, "industry_callback_rate.csv")
    df.to_csv(filename, index=False)

    print("\n" + "="*50)
    print("  CALLBACK RATE BY INDUSTRY")
    print("="*50)
    print(df.to_string(index=False))
    print("="*50)
    print(f"[Report] Saved → {filename}\n")
    return df


# ── REPORT 4: Top Job Sources ─────────────────────────────────────────────────

def report_top_sources():
    data = top_sources()
    if not data:
        print("[Report] No source data available.")
        return
    df = pd.DataFrame(data)
    ensure_reports_dir()
    filename = os.path.join(REPORTS_DIR, "top_sources.csv")
    df.to_csv(filename, index=False)

    print("\n" + "="*50)
    print("  TOP JOB SOURCES")
    print("="*50)
    print(df.to_string(index=False))
    print("="*50)
    print(f"[Report] Saved → {filename}\n")
    return df


# ── REPORT 5: Status Summary ──────────────────────────────────────────────────

def report_status_summary():
    data = status_summary()
    if not data:
        print("[Report] No status data available.")
        return
    df = pd.DataFrame(data)
    ensure_reports_dir()
    filename = os.path.join(REPORTS_DIR, "status_summary.csv")
    df.to_csv(filename, index=False)

    print("\n" + "="*50)
    print("  APPLICATION STATUS SUMMARY")
    print("="*50)
    print(df.to_string(index=False))
    print("="*50)
    print(f"[Report] Saved → {filename}\n")
    return df


# ── GENERATE ALL REPORTS AT ONCE ──────────────────────────────────────────────

def generate_all_reports():
    print("\n[Reports] Generating all reports...\n")
    report_all_applications()
    report_weekly_summary()
    report_industry_callback()
    report_top_sources()
    report_status_summary()
    print("[Reports] All reports generated successfully in /reports folder.\n")