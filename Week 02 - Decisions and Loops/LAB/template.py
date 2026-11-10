"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 08/11/2026

Run it:   python template.py
"""

over_limit_count = 0

while True:

    # ==================================================================== INPUT

    label = input("Enter record name (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))


    # ================================================================== PROCESS

    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    # =================================================================== OUTPUT

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

print("Total records OVER LIMIT:", over_limit_count)
