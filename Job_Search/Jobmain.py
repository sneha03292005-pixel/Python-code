"""
main.py — CLI entry point for Smart Job Tracker
Smart Job Tracker | Sneha B

Run:  python main.py
"""

from db import (
    setup_database, insert_job, fetch_all_jobs,
    search_jobs, filter_by_status, update_status, delete_job
)
from data_handler import import_csv_to_db, load_and_clean_csv, analyse_dataframe
from reports import generate_all_reports


# ── DISPLAY HELPERS ───────────────────────────────────────────────────────────

def print_header():
    print("\n" + "="*55)
    print("       SMART JOB TRACKER — Sneha B")
    print("="*55)


def print_jobs(jobs):
    if not jobs:
        print("  No records found.\n")
        return
    print(f"\n  {'ID':<4} {'Company':<20} {'Role':<22} {'Status':<12} {'Response'}")
    print("  " + "-"*75)
    for j in jobs:
        print(f"  {j['id']:<4} {j['company']:<20} {j['role']:<22} {j['status']:<12} {j['response']}")
    print()


# ── MENU ACTIONS ──────────────────────────────────────────────────────────────

def add_job_manually():
    print("\n── Add New Application ──────────────────────────────")
    company    = input("  Company name   : ").strip()
    role       = input("  Role applied   : ").strip()
    industry   = input("  Industry       : ").strip() or "Unknown"
    source     = input("  Source (LinkedIn/Naukri etc.) : ").strip() or "Unknown"
    applied_on = input("  Date applied (YYYY-MM-DD)     : ").strip() or "Unknown"
    insert_job(company, role, industry, source, applied_on)
    print("  ✔ Job application added.\n")


def view_all():
    print("\n── All Applications ─────────────────────────────────")
    print_jobs(fetch_all_jobs())


def search():
    keyword = input("\n  Enter keyword (company or role): ").strip()
    print_jobs(search_jobs(keyword))


def filter_status():
    status = input("\n  Filter by status (Applied / Interview / Offer / Rejected): ").strip()
    print_jobs(filter_by_status(status))


def update():
    job_id   = input("\n  Enter Job ID to update: ").strip()
    status   = input("  New status   : ").strip()
    response = input("  New response : ").strip()
    update_status(int(job_id), status, response)
    print("  ✔ Record updated.\n")


def delete():
    job_id = input("\n  Enter Job ID to delete: ").strip()
    delete_job(int(job_id))
    print("  ✔ Record deleted.\n")


def import_csv():
    path = input("\n  Enter CSV file path (e.g. sample_data.csv): ").strip()
    import_csv_to_db(path)


def run_eda():
    path = input("\n  Enter CSV file path for EDA: ").strip()
    df = load_and_clean_csv(path)
    analyse_dataframe(df)


# ── MAIN MENU ─────────────────────────────────────────────────────────────────

def main():
    setup_database()
    while True:
        print_header()
        print("  1. Add job application")
        print("  2. View all applications")
        print("  3. Search applications")
        print("  4. Filter by status")
        print("  5. Update application status")
        print("  6. Delete application")
        print("  7. Import from CSV")
        print("  8. Run EDA on CSV")
        print("  9. Generate all reports")
        print("  0. Exit")
        print("-"*55)
        choice = input("  Choose option: ").strip()

        if   choice == "1": add_job_manually()
        elif choice == "2": view_all()
        elif choice == "3": search()
        elif choice == "4": filter_status()
        elif choice == "5": update()
        elif choice == "6": delete()
        elif choice == "7": import_csv()
        elif choice == "8": run_eda()
        elif choice == "9": generate_all_reports()
        elif choice == "0":
            print("\n  Bye! Keep applying. You got this 💪\n")
            break
        else:
            print("  Invalid option. Try again.\n")


if __name__ == "__main__":
    main()