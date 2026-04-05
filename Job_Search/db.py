"""
db.py — Database setup and all SQL query functions
Smart Job Tracker | Sneha B
"""

import sqlite3
import os

DB_NAME = "job_tracker.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def setup_database():
    """Create the jobs table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            company     TEXT    NOT NULL,
            role        TEXT    NOT NULL,
            industry    TEXT,
            source      TEXT,
            applied_on  TEXT,
            status      TEXT    DEFAULT 'Applied',
            response    TEXT    DEFAULT 'No Response'
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Database ready.")


# ── INSERT ────────────────────────────────────────────────────────────────────

def insert_job(company, role, industry, source, applied_on, status="Applied", response="No Response"):
    conn = get_connection()
    conn.execute("""
        INSERT INTO jobs (company, role, industry, source, applied_on, status, response)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (company, role, industry, source, applied_on, status, response))
    conn.commit()
    conn.close()


# ── READ ──────────────────────────────────────────────────────────────────────

def fetch_all_jobs():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM jobs ORDER BY applied_on DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def search_jobs(keyword):
    """Search by company name or role (case-insensitive)."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM jobs
        WHERE LOWER(company) LIKE ? OR LOWER(role) LIKE ?
        ORDER BY applied_on DESC
    """, (f"%{keyword.lower()}%", f"%{keyword.lower()}%")).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def filter_by_status(status):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM jobs WHERE LOWER(status) = ? ORDER BY applied_on DESC",
        (status.lower(),)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ── UPDATE ────────────────────────────────────────────────────────────────────

def update_status(job_id, new_status, new_response):
    conn = get_connection()
    conn.execute(
        "UPDATE jobs SET status = ?, response = ? WHERE id = ?",
        (new_status, new_response, job_id)
    )
    conn.commit()
    conn.close()


# ── DELETE ────────────────────────────────────────────────────────────────────

def delete_job(job_id):
    conn = get_connection()
    conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()


# ── ANALYTICS QUERIES ─────────────────────────────────────────────────────────

def response_rate_by_industry():
    """
    JOIN-style aggregation: total applications and callback count per industry.
    Calculates callback rate (%).
    """
    conn = get_connection()
    rows = conn.execute("""
        SELECT
            industry,
            COUNT(*) AS total_applied,
            SUM(CASE WHEN response != 'No Response' THEN 1 ELSE 0 END) AS total_responses,
            ROUND(
                100.0 * SUM(CASE WHEN response != 'No Response' THEN 1 ELSE 0 END) / COUNT(*),
                2
            ) AS callback_rate_pct
        FROM jobs
        GROUP BY industry
        HAVING total_applied > 0
        ORDER BY callback_rate_pct DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def top_sources():
    """Which job source (LinkedIn, Naukri, etc.) gives the most responses."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT
            source,
            COUNT(*) AS total_applied,
            SUM(CASE WHEN response != 'No Response' THEN 1 ELSE 0 END) AS callbacks
        FROM jobs
        GROUP BY source
        ORDER BY callbacks DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def weekly_stats():
    """Applications grouped by week (using applied_on date)."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT
            strftime('%Y-W%W', applied_on) AS week,
            COUNT(*) AS applications,
            SUM(CASE WHEN status = 'Interview' THEN 1 ELSE 0 END) AS interviews,
            SUM(CASE WHEN status = 'Offer' THEN 1 ELSE 0 END) AS offers
        FROM jobs
        WHERE applied_on IS NOT NULL
        GROUP BY week
        ORDER BY week DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def status_summary():
    """Count of each application status."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT status, COUNT(*) AS count
        FROM jobs
        GROUP BY status
        ORDER BY count DESC
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]