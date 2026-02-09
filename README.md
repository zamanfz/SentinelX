# SentinelX 🚨  
### Lightweight Service Monitoring with Live Dashboard

SentinelX is a Python-based service monitoring system designed to continuously track the health of critical services and present their status in a clean, real-time dashboard.

## 🔍 Why SentinelX?
Modern systems rely on multiple background services. SentinelX provides:
- Real-time visibility into service health
- Minimal overhead (no Docker, no heavy agents)
- Simple architecture suitable for constrained environments (VMs, servers, labs)

## 🧠 Architecture Overview
- **Service Probes**: Lightweight Python checks for each service
- **Monitor Engine**: Periodically evaluates service health
- **Live Dashboard**: Web UI showing current status and last check time

- ## 📊 Dashboard Features
- Live service status (OK / DOWN)
- Last-checked timestamp
- Auto-refreshing UI
- Clean, dark-themed interface

## 🛠 Tech Stack
- Python 3
- Flask (dashboard)
- HTML/CSS (UI)
- Linux (RHEL / VM tested)

## 📁 Project Structure
SentinelX/
├── monitor/
│   ├── app.py
│   └── monitor.py
│
├── services/
│   ├── service_a.py
│   └── service_b.py
│
└── README.md

## Author

**Fahim Zaman**  
Computer Science Engineer  
GitHub: https://github.com/zamanfz

## 🚀 How to Run
```bash
python3 monitor/app.py

