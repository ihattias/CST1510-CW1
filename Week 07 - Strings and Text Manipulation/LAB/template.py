"""
RECORD CHECK - my version

Name : Isaac Attias
Lane : IT
Date : 10/11/2026
"""

# ================================================= FUNCTIONS

def parse_line(raw_line):
    """Clean a messy record and return a dictionary."""

    parts = raw_line.strip().split(",")

    record = {"hostname": parts[0].strip().lower()}

    for part in parts[1:]:
        key, value = part.split("=")
        record[key.strip().lower()] = float(value.strip())

    return record


def status_of(record):
    """Return the status of a record."""

    percent = (record["used"] / record["total"]) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ================================================= INPUT

raw_records = []

with open("my_messy_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)


# ====================================== PROCESS + OUTPUT

total = 0
flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record, "-", status)

    total += 1

    if status != "OK":
        flagged += 1

print()
print("Total records:", total)
print("Flagged records:", flagged)