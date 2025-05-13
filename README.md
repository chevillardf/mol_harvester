# 🧪 mol_harvester

**mol_harvester** is a data engineering project designed to extract, transform, and load large molecular data from **SureChemBL**. The goal is to build a scalable and modular ETL pipeline using modern **Apache big data tools**.

This project is ideal for exploring chemical space data, with an emphasis on patent-sourced molecules..

---

## 🚀 Project Goals

- Build a structured **ETL pipeline** to process large molecular datasets
- Use industry-standard **Apache tooling** for each stage
- Enable fast prototyping for cheminformatics and ML-ready data

---

## 🔧 Apache Tooling Integration Plan

| Stage        | Tool(s)         | Role                                                                 |
|--------------|-----------------|----------------------------------------------------------------------|
| **Storage**   | 🧱 HDFS          | Store raw and intermediate SureChemBL data (e.g., Parquet)           |
| **Ingestion** | 🔄 Kafka | Simulate streaming updates (e.g., new patents)                       |
| **Processing**| ⚡ Spark         | Transform, clean, and join data at scale                             |
| **Querying**  | 🐝 Hive          | Define warehouse schema, enable SQL queries                          |
| **Orchestration** | 📅 Airflow   | Automate ETL workflows (e.g., extract ➝ transform ➝ load)            |

---

## 📁 Project Structure
'''
mol_harvester/
├── data/
│ ├── lake/
│ │ ├── SureChemBL
│ │ └── ...
│ └── warehouse/ # Structured, analytics-ready data (via Hive)
├── etl/ # Extraction and transformation logic
├── spark_jobs/ # Spark-based processing scripts
├── airflow/ # Airflow DAGs for orchestration
├── hive/ # Hive table definitions
├── kafka/ # Kafka utilities (optional)
└── README.md
'''
---

## 🗺️ Status

✅ Data sources (SureChemBL)  
🔜 Transformation using Spark  
🔜 Warehouse definition with Hive

---

## 📌 Notes

- This project assumes access to a working Apache stack (e.g., Hadoop, Spark, Hive).
- For local development, Docker and/or Minikube setups can be used to simulate the environment.


