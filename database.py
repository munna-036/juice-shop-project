import sqlite3

conn = sqlite3.connect("security_alerts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    finding TEXT,
    severity TEXT,
    target TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Security alert database created successfully.")
