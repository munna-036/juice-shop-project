import sqlite3
from datetime import datetime

conn = sqlite3.connect("security_alerts.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO alerts
(timestamp, finding, severity, target, status)
VALUES (?, ?, ?, ?, ?)
""", (
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Security Misconfiguration",
    "Medium",
    "Authorized Lab Target",
    "Open"
))

conn.commit()
conn.close()

print("Security alert logged successfully.")
