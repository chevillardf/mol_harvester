from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from chembl_webresource_client.new_client import new_client

def fetch_chembl_assays():
    assay = new_client.assay
    batch_size = 20
    offset = 0
    max_records = 1000  # adjust as needed

    results = []
    while True:
        batch = assay.filter(
            assay_type='A',
            assay_organism__iexact='Homo sapiens'
        ).only(['assay_type', 'description', 'assay_chembl_id', 'assay_organism'])[offset:offset + batch_size]

        batch = list(batch)
        if not batch:
            break
        results.extend(batch)

        offset += batch_size
        if offset >= max_records:
            break

    df = pd.DataFrame(results)
    df.to_csv('~/Documents/projects/mol_harvester/data/staging/test_etl.csv', index=False)

default_args = {
    'start_date': datetime(2025, 1, 1),
    'owner': 'florent'
}

with DAG('chembl_assay_etl',
         schedule_interval=None,
         default_args=default_args,
         catchup=False,
         description='Fetch ChEMBL Type A assays for Homo sapiens',
         tags=['chembl', 'etl']) as dag:

    extract_task = PythonOperator(
        task_id='fetch_chembl_assays',
        python_callable=fetch_chembl_assays
    )

    extract_task