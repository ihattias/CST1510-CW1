
"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 09/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the formatted record report."""
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


over_limit_count = 0

while True:

    # ==================================================================== INPUT

    label = input("Enter record name (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))


    # ================================================================== PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)


    # =================================================================== OUTPUT

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print("Total records OVER LIMIT:", over_limit_count)
