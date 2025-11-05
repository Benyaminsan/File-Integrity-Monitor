import os
import json
import hashlib
from datetime import datetime

HASH_DB = "hash_db.json"
LOG_FILE = "security.log"
MONITOR_DIR = "secure_files"


def calculate_hash(file_path):
    """Hitung SHA256 hash dari file"""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_baseline():
    """Muat hash database"""
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as f:
        return json.load(f)


def save_baseline(baseline):
    """Simpan hash database"""
    with open(HASH_DB, "w") as f:
        json.dump(baseline, f, indent=4)


def log_event(level, message):
    """Catat ke security.log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {level}: {message}\n"
    with open(LOG_FILE, "a") as log:
        log.write(log_line)


def scan_and_detect():
    """Scan folder dan deteksi perubahan"""
    baseline = load_baseline()
    current_files = {}
    results = {"INFO": [], "WARNING": [], "ALERT": []}

    # Hitung hash semua file yang ada saat ini
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            current_files[file] = file_hash

            if file not in baseline:
                msg = f'Unknown file "{file}" detected.'
                log_event("ALERT", msg)
                results["ALERT"].append(msg)
            elif baseline[file] != file_hash:
                msg = f'File "{file}" integrity failed!'
                log_event("WARNING", msg)
                results["WARNING"].append(msg)
            else:
                msg = f'File "{file}" verified OK.'
                log_event("INFO", msg)
                results["INFO"].append(msg)

    # Deteksi file yang dihapus
    for file in baseline.keys():
        if file not in current_files:
            msg = f'File "{file}" deleted or missing.'
            log_event("ALERT", msg)
            results["ALERT"].append(msg)

    # Update baseline
    save_baseline(current_files)
    return results


def analyze_log():
    """Analisis security.log"""
    if not os.path.exists(LOG_FILE):
        return {"safe": 0, "corrupted": 0, "anomalies": 0, "last_anomaly": "N/A"}

    safe = corrupted = anomalies = 0
    last_anomaly = "N/A"

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "INFO:" in line:
                safe += 1
            elif "WARNING:" in line:
                corrupted += 1
                last_anomaly = line.split("]")[0][1:]
            elif "ALERT:" in line:
                anomalies += 1
                last_anomaly = line.split("]")[0][1:]

    return {
        "safe": safe,
        "corrupted": corrupted,
        "anomalies": anomalies,
        "last_anomaly": last_anomaly,
    }

if __name__ == "__main__":
    results = scan_and_detect()
    print("Hasil pemindaian:")
    for level, messages in results.items():
        print(f"\n{level}:")
        for msg in messages:
            print(" -", msg)

    summary = analyze_log()
    print("\nRingkasan log:")
    print(summary)
