from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def retrain_model():
    subprocess.run(["python3", "/opt/airflow/model_training/train_model.py"], check=True)

default_args = {
    'owner': 'yash',
    'start_date': datetime(2025, 7, 7),
    'retries': 1,
}

with DAG(
    'salary_model_retraining',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False
) as dag:

    retrain_task = PythonOperator(
        task_id='retrain_model',
        python_callable=retrain_model
    )
