from flask import Flask, render_template, redirect, url_for
import os
from monitor import scan_and_detect, analyze_log

app = Flask(__name__)

LOG_FILE = "security.log"


def read_logs():
    """Baca log dari security.log dan parse ke list"""
    if not os.path.exists(LOG_FILE):
        return []

    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                # Format: [2025-10-30 13:25:11] LEVEL: Message
                timestamp = line.split("]")[0][1:]
                level = line.split("]")[1].split(":")[0].strip()
                message = ":".join(line.split(":")[1:]).strip()
                logs.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message
                })
            except Exception:
                continue
    return logs


@app.route("/")
def index():
    summary = analyze_log()
    logs = read_logs()
    return render_template("index.html", summary=summary, logs=logs)


@app.route("/scan")
def scan():
    scan_and_detect()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
