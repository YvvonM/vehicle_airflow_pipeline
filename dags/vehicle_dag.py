#importing libraries
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from dbt.contrib.operators.run import DbtRunOperator
from src.get_csv_data import get_csv_data

# Define the default dag arguments.
default_args = {
    'owner': 'Admin',
    'depends_on_past': False,
    'email': ['yvvonjemymahmajala@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
dag_id = 'vehicle_db_dag', default_args=default_args,
    start_date=datetime(2023, 12, 22),
    schedule_interval= '@daily'
) as dag:
    
    load_data = PythonOperator(
        task_id = 'get_csv_data',
        python_callable= get_csv_data
        
    )
    transform_data = DbtRunOperator(
        task_id = 'transform_data',
        dir=r'C:\Users\User\Documents\airflow\vehicle\models\vehiclessql',  # Path to your dbt models directory
        profiles_dir=r'C:\Users\User\Documents\airflow\vehicle\profiles.yml'
    )
load_data >> transform_data



