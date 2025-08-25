# 🌱 Smart Farm IoT Monitoring (AWS IoT + QuickSight)

A cloud-based prototype that simulates farm sensors (temperature, moisture, pH), ingests data via AWS IoT Core, stores it in DynamoDB, queries with Athena, visualizes with QuickSight, and sends alerts via SNS.

---

## 🚀 Architecture
![Architecture Diagram](architecture/smart-farm-architecture-hd.png)

---

## 🛠️ Features
- **Sensor Simulation**: Python script publishing random farm data via MQTT/TLS.
- **AWS IoT Core**: Secure device authentication + rules.
- **Data Ingestion**: IoT Rule → DynamoDB.
- **Analytics**: DynamoDB queried with Athena (via Federated Connector + Glue).
- **Visualization**: QuickSight dashboards (line charts, KPIs, thresholds).
- **Alerts**: SNS email notifications when conditions breach safe ranges.
- **Security**: TLS certs, IAM roles, least-privilege IoT policies.

---

## 📊 Dashboard
- **Sheet 1**: Line charts for trends with safe thresholds.
- **Sheet 2**: KPI cards for latest values with conditional formatting.

📌 *Screenshots available in* [`docs/screenshots/`](docs/screenshots/)

---

## 📡 Alerts
Configured thresholds:
- Temperature > 35°C
- Moisture < 30%
- pH outside 6.0–7.0

👉 Email alert triggered via Amazon SNS.

---

## ⚡ Challenges & Workarounds
- ❌ Timestream not available to new users.  
- ❌ IoT Analytics blocked for new customers.  
- ❌ DynamoDB no longer a native QuickSight connector.  
- ✅ Solution: DynamoDB → Athena Federated Connector → QuickSight.

---

## 📂 Repository Contents
- `simulator/` → Python scripts for simulating IoT sensor data.  
- `architecture/` → Final architecture diagrams (HD PNG + SVG).  
- `docs/` → Detailed report, executive summary, screenshots.  

---

## 📖 Documentation
- [Detailed Report](docs/FINAL_REPORT.md)  
- [Executive Summary](docs/EXEC_SUMMARY.md)  

---

## 🔒 Security
- Do **NOT** commit AWS certs or private keys.  
- `.gitignore` excludes sensitive files in `simulator/certs/`.

---

## 📌 Future Enhancements
- Forecasting with QuickSight / Amazon Forecast.  
- Mobile/React Dashboard.  
- ML-based anomaly detection.  
- Multi-device scalability.

---

## 📝 License
This project is licensed under the [MIT License](LICENSE).
