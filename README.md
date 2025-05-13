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
| **Storage**   | 🧱 Hadoop          | Store raw and intermediate data           |
| **Ingestion** | 🔄 Kafka | Simulate streaming updates (i.e. new patents)                       |
| **Processing**| ⚡ Spark         | Transform, clean, and join data at scale                             |
| **Querying**  | 🐝 Hive          | Define warehouse schema, enable SQL queries                          |
| **Orchestration** | 📅 Airflow   | Automate ETL workflows            |

---

## 📁 Project Structure

```text
mol_harvester/
├── data/
│   ├── lake/                  # Raw data files
│   │   ├── SureChemBL/        
│   │   └── ...                
│   └── warehouse/             # Structured, processed data
├── etl/                       # Extraction, transformation and loading logic
├── spark_jobs/                # Spark-based processing scripts
├── airflow/                   # Airflow DAGs for orchestration
├── hive/                      # Hive table definitions
├── kafka/                     # Kafka utilities
└── README.md                  
```
---

## 🗺️ Status

✅ Data sources (SureChemBL)  
🔜 Transformation using Spark  
🔜 Warehouse definition with Hive

---

## 📌 Notes

- This project assumes access to a working Apache stack (Hadoop, Spark, Hive, ...).
- For local development, Docker can be used to simulate the environment.


