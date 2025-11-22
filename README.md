# Databricks DLT Taxi Pipeline — Mini Assignment

This repository contains the Delta Live Tables (DLT) pipeline for the Taxi Trip Analytics project, covering Bronze → Silver → Gold layers, weekly aggregations, suspicious ride detection, and data quality validation.

---

## Repository Structure

dlt_taxi_pipeline_assignment/
│

├── dlt_taxi_project/

│ ├── 01_bronze_ingest_dlt.py

│ ├── 02_silver_transformations.py

│ ├── 03_gold_materialized.py

│ └── taxi_sample.csv


├── validation_queries.ipynb


├── dlt_taxi_pipeline/

│ ├── pipeline_configuration.json

│ ├── pipeline_graph.png


└── README.md

---

## Pipeline Overview

### **Bronze Layer**
- Ingests raw taxi trip data into `bronze_taxi`
- Applies quality rule: `trip_distance > 0`
- Reads from `workspace.default.taxi_sample`

### **Silver Layer**
- Creates cleaned table: `silver_taxi_clean`
- Flags suspicious rides based on fare-to-distance ratio
- Creates weekly aggregates: `silver_weekly_agg`

### **Gold Layer**
- Materialized view: `gold_top3_fares`
- Contains top 3 highest fare rides with passenger details

---

## Validation Notebook

`validation_queries.py` verifies:
- Bronze row count
- Distance quality checks
- Suspicious ride detection
- Weekly aggregates
- Top 3 fare rides
- Python assertions

---

## Lineage Graph

The `pipeline_graph.png` includes the DLT DAG:

bronze_taxi

↓

silver_taxi_clean → silver_weekly_agg

↓

gold_top3_fares

---

## How to Run the Pipeline

1. Open Databricks → Pipelines  
2. Select `dlt_taxi_pipeline`  
3. Click **Run Pipeline**  
4. Wait until all tables turn green  
5. Execute `validation_queries.py` manually

---

## Submission Contents

1. Notebooks (Python source files)  
2. Data file (`taxi_sample.csv`)  
3. Pipeline configuration  
4. Pipeline graph image  
5. README with full documentation  

---

## Author

**Toparam Srenitha**  
Databricks DLT Mini Assignment  
