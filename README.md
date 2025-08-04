# ✈️ Live Aerospace Maintenance Data Project

This project combines **real-time aircraft data** from the OpenSky Network API with **historical maintenance issue reports** from the FAA SDR (Service Difficulty Reports) dataset to identify and analyze aircraft with a history of technical problems.

## 🚀 Project Goal

To simulate a live aircraft monitoring system that:
- Tracks real-time aircraft globally
- Merges with maintenance history data
- Highlights aircraft with repeated issues
- Performs EDA to assess safety & reliability trends

---

## 🧩 Features

- 🔄 Live aircraft data via OpenSky API
- 🛠 Historical issue data from FAA SDR
- 📊 Visual analysis of aircraft component failures
- 🚨 Flagging of aircraft with frequent problems
- 📈 Insights by aircraft model, component, and manufacturer

---

## 📁 Project Structure

live_maintenance_eda/
├── data/
│ └── faa_sdr_sample.csv # Historical maintenance data
├── scripts/
│ ├── fetch_opensky_live_data.py # Fetch live aircraft data
│ └── merge_live_and_historical_data.py # Merge live and SDR data
├── notebooks/
│ └── eda_analysis.ipynb # EDA notebook for insights
├── main.py # Main script to run the pipeline
├── requirements.txt # Python dependencies
└── README.md # Project overview

