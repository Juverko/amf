from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'coder2j',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_hello():
    print("Hello World!!!!!!!!!!!!!!!!!")


def get_plugin():
    from airflow_clickhouse_plugin.operators.clickhouse import ClickHouseOperator
    print(f"clickhouseOperator!!!!!!! with version: {ClickHouseOperator.__class__}")


with DAG(
    default_args=default_args,
    dag_id="dag_with_python_dependencies_v05",
    start_date=datetime(2021, 10, 12),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='get_hello',
        python_callable=get_hello
    )
    
    task2 = PythonOperator(
        task_id='get_plugin',
        python_callable=get_plugin
    )

    task1 >> task2