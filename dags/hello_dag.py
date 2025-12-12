from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="hello_crypto",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="say_hi",
        bash_command="echo 'Airflow working'",
    )
