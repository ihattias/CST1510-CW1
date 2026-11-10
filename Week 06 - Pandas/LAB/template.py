"""
RECORD CHECK  -  my version
===========================

Name  : Isaac Attias
Lane  : IT
Date  : 10/11/2026

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD

df = pd.read_csv("my_records.csv")


# ================================================================= PROCESS

df["percent"] = (df["value"] / df["limit"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT

print(df)

print()
print("Records requiring attention:")
print(df[df["status"] != "OK"])

print()
print("Records by status:")
counts = df.groupby("status")["label"].count()
print(counts)

df.to_csv("my_records_report.csv", index=False)

counts.plot(kind="bar", title="Records by Status")
plt.tight_layout()
plt.savefig("my_records_chart.png")
plt.show()