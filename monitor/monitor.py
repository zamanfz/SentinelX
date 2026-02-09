from flask import Flask, jsonify
from threading import Thread
import time, requests
from datetime import datetime

SERVICE_STATUS = {
    "service_a": {"status": "INIT", "last_checked": None},
    "service_b": {"status": "INIT", "last_checked": None},
}

SERVICES = {
    "service_a":
"http://localhost:5001/health",
    "service_b":
"http://localhost:5002/health"
}

def check_services():
    for name, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=2)
            status = r.json().get("status", "UNKNOWN")
            SERVICE_STATUS[name]["status"] = status
            SERVICE_STATUS[name]["last_checked"] = datetime.now().strftime("%H:%M:%S")
            if status != "OK":
                print(f"ALERT: {name} is UNHEALTHY ({status})")
            else:
                print(f"{name} is healthy")
        except Exception as e:
            print(f"ERROR: {name} unreachable ({e})")

api = Flask(__name__)

@api.route("/status")
def status():
    return jsonify(SERVICE_STATUS)

def run_api():
    api.run(port=7000)


if __name__== "__main__":
    print("SentinelX Monitor started\n")
    Thread(target=run_api, daemon=True).start()
    while True:
        check_services()
        print("-" * 40)
        time.sleep(5)


