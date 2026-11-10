
"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 09/11/2026

Run it:   python template.py
"""

# ====================================================================== CLASS

class Record:
    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status of this record."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Load a list of Record objects from a file."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records


records = load_records("records_sample.txt")


# ==================================================================== OUTPUT

over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"Value  : {record.value:>10.2f}")
    print(f"Limit  : {record.limit:>10.2f}")
    print(f"Status : {record.status()}")

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)

print("Total records OVER LIMIT:", over_limit_count)
