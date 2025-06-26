# 🧪 mol_harvester

**mol_harvester** is a scalable ETL pipeline for processing large-scale molecular data from ChemBL, built using modern Apache data engineering tools.

---

## 🚀 Project Goals

- Build a structured **ETL pipeline** to process large molecular datasets
- Use industry-standard **Apache tooling** for each stage
- Enable fast prototyping for cheminformatics and ML-ready data

---

## 🔧 Apache Tooling Integration Plan

| Stage        | Tool(s)         | Role                                                                 |
|--------------|-----------------|----------------------------------------------------------------------|
| **Storage**   | 🧱 Hadoop          | Store raw and intermediate data           |
| **Ingestion** | 🔄 Kafka | Updates                       |
| **Processing**| ⚡ Spark         | Transform data at scale                             |
| **Querying**  | 🐝 Hive          | Define warehouse schema, enable SQL queries                          |
| **Orchestration** | 📅 Airflow   | Automate ETL workflows            |

---

## 📁 Project Structure

```text
mol_harvester/
├── data/
│   ├── raw/
│   ├── staging/
│   └── processed/
├── etl/
├── spark_jobs/                
├── airflow/
├── hive/
├── kafka/
└── README.md
```
---

## 🗺️ Status

✅ Data sources (ChemBL)
🔜 ETL MVP

---

## 📌 Notes

- This project assumes access to a working Apache stack (Hadoop, Spark, Hive, ...).
- For local development, Docker can be used to simulate the environment.


