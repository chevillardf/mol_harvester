# 🧪 mol_harvester

**mol_harvester** is a scalable ETL pipeline for processing large-scale molecular data from SureChemBL patents, built using modern Apache data engineering tools.

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
| **Ingestion** | 🔄 Kafka | Updates (i.e. new patents)                       |
| **Processing**| ⚡ Spark         | Transform, clean, and join data at scale                             |
| **Querying**  | 🐝 Hive          | Define warehouse schema, enable SQL queries                          |
| **Orchestration** | 📅 Airflow   | Automate ETL workflows            |

---

## 📁 Project Structure

```text
mol_harvester/
├── data/
│   ├── raw/                  # Raw data files
│   │   ├── SureChemBL/        
│   │   └── ...                
│   └── processed/             # Structured, processed data
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


