from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_alerts():
    conn = sqlite3.connect("security_alerts.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM alerts ORDER BY id DESC"
    )

    alerts = cursor.fetchall()
    conn.close()

    return alerts


@app.route("/")
def dashboard():
    alerts = get_alerts()
    return render_template(
        "dashboard.html",
        alerts=alerts
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
