import sqlite3
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


DATABASE = "security_alerts.db"
OUTPUT = "reports/security_audit_report.pdf"

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

cursor.execute("""
SELECT timestamp, finding, severity, target, status
FROM alerts
ORDER BY id DESC
""")

alerts = cursor.fetchall()

conn.close()


doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4
)

styles = getSampleStyleSheet()

story = []

story.append(
    Paragraph(
        "Security Audit Report",
        styles["Title"]
    )
)

story.append(
    Paragraph(
        "Automated Web Security Assessment",
        styles["Heading2"]
    )
)

story.append(
    Paragraph(
        "Generated: " +
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        styles["Normal"]
    )
)

story.append(Spacer(1, 20))


data = [
    ["Timestamp", "Finding", "Severity", "Target", "Status"]
]

for alert in alerts:
    data.append(list(alert))


table = Table(data)

table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP")
    ])
)

story.append(table)

doc.build(story)

print("PDF audit report generated successfully.")
