from flask import Flask, render_template, redirect, url_for
from monitor import scan_and_detect, analyze_log
import os

app = Flask(__name__)

@app.route("/")
def index():
    summary = analyze_log()
    return render_template("index.html", summary=summary)

@app.route("/scan")
def scan():
    scan_and_detect()
    return redirect(url_for("index"))

if __name__ == "__main__":
    os.makedirs("secure_files", exist_ok=True)
    app.run(debug=True)
