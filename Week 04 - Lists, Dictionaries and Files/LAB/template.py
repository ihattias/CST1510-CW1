
"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 09/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def check_record(value, limit):
    """Return the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value      : {value:>10.2f}")
    print(f"Limit      : {limit:>10.2f}")
    print(f"Difference : {difference:>10.2f}")
    print(f"Percentage : {percent:>10.2f}%")
    print(f"Status     : {status}")
    print("=" * 34)


def load_records(path):
    """Load records from a text file."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })

    return records


def print_summary(count):
    """Print the number of records over the limit."""
    print("Total records OVER LIMIT:", count)


# ====================================================================== STORE

records = load_records("records_sample.txt")


# =============================================================== PROCESS + OUTPUT

over_limit_count = 0

with open("results.txt", "w") as f:
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]

        difference, percent, status = check_record(value, limit)

        print_report(label, value, limit, difference, percent, status)

        f.write(f"{label},{status}\n")

        if status == "OVER LIMIT":
            over_limit_count += 1

print_summary(over_limit_count)
