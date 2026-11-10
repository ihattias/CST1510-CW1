
"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 08/11/2026

Run it:   python template.py
"""

# ==================================================================== INPUT

label = input("Enter record name: ")
first = float(input("Enter first value: "))
second = float(input("Enter second value: "))


# ================================================================== PROCESS

difference = first - second
percent = (first / second) * 100


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"First value  : {first:>10.2f}")
print(f"Second value : {second:>10.2f}")
print(f"Difference   : {difference:>+10.2f}")
print(f"Percentage   : {percent:>10.2f}%")
print("Record check completed")

print("=" * 34)
