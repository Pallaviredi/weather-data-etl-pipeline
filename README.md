# 🌦️ Weather Data ETL Pipeline

## 📌 Overview

This project is an end-to-end **ETL (Extract, Transform, Load) pipeline** that collects weather data from an external API, processes it, and stores it for analysis.

The pipeline is designed with a modular architecture to simulate real-world **data engineering workflows**.

---

## 🏗️ Architecture

```
        API (Weather Data)
                ↓
            Extract
                ↓
           Transform
                ↓
              Load
                ↓
         Storage (CSV/DB)
```

---

## ⚙️ Tech Stack

* Python
* Requests (API calls)
* Pandas (data transformation)
* CSV / SQLite (storage)
* Git (version control)
* Scheduler (Cron / Task Scheduler)

---

## 📂 Project Structure

```
weather-data-etl-pipeline/
│
├── data/              # Output files
├── logs/              # Log files
├── config/            # Configuration files
│   └── config.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 How It Works

1. **Extract**
   Fetch weather data from API

2. **Transform**
   Clean and structure the data

3. **Load**
   Store data into CSV or database

---

## ▶️ How to Run

```bash
git clone <repo-url>
cd weather-data-etl-pipeline
pip install -r requirements.txt
python scripts/main.py
```

---

## 🔄 Automation

The pipeline can be scheduled to run periodically using:

* Cron (Linux/Mac)
* Task Scheduler (Windows)

---

## 📊 Future Enhancements

* Add database support (PostgreSQL)
* Integrate Apache Airflow for orchestration
* Store data in cloud (AWS S3)
* Add dashboard (Power BI / Tableau)

---

## 🧠 Key Learnings

* Building ETL pipelines
* API integration
* Data transformation
* Automation & scheduling
* Project structuring

---

## 👤 Author

Your Name
Pallavi Reddy
