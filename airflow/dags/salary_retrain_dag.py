from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import ShortCircuitOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

# === DAG Default Arguments ===
default_args = {
    'owner': 'Yash_Rajput',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

# === Python Function to Check Drift Flag ===
def is_drift_detected():
    flag_path = "/opt/airflow/flags/drift_detected.txt"
    try:
        with open(flag_path, "r") as f:
            result = f.read().strip().lower() == "yes"
            print(f"[INFO] Drift detected: {result}")
            return result
    except FileNotFoundError:
        print("[WARNING] Drift flag file not found.")
        return False

# === DAG Definition ===
with DAG(
    dag_id='salary_forecasting',
    default_args=default_args,
    description='Pipeline to detect drift, retrain and register salary prediction model',
    schedule_interval='@hourly',
    start_date=datetime(2025, 7, 1),
    catchup=False,
    tags=['salary', 'mlops', 'automation'],
) as dag:

    # 1. Wait for new data file to arrive
    wait_for_data_file = FileSensor(
        task_id='wait_for_salary_data',
        filepath='/opt/airflow/data/new_salary_data.csv',
        poke_interval=30,
        timeout=600,
        mode='poke'
    )

    # 2. Run data drift detection script
    run_drift_detection = BashOperator(
        task_id='run_drift_detection',
        bash_command='echo "[INFO] Executing drift detection script..." && python /opt/airflow/dags/detect_drift.py'
    )

    # 3. Check if drift was detected
    evaluate_drift_flag = ShortCircuitOperator(
        task_id='evaluate_drift_flag',
        python_callable=is_drift_detected
    )

    # 4. Train the updated model
    execute_model_training = BashOperator(
        task_id='execute_model_training',
        bash_command='echo "[INFO] Training updated salary prediction model..." && python /opt/airflow/dags/train_model.py'
    )

    # 5. Register model to MLflow
    perform_model_registration = BashOperator(
        task_id='perform_model_registration',
        bash_command='echo "[INFO] Registering updated model to MLflow..." && python /opt/airflow/dags/register_model.py'
    )

    # === DAG Flow ===
    wait_for_data_file >> run_drift_detection >> evaluate_drift_flag >> execute_model_training >> perform_model_registration
