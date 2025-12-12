from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_and_save_crypto():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {"X-CMC_PRO_API_KEY": API_KEY}
    params = {"start": "1", "limit": "15", "convert": "USD"}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]
    
    df = pd.json_normalize(data)
    df["fetch_timestamp"] = datetime.now()
    
    engine = create_engine("postgresql://airflow:airflow@postgres/airflow")
    df.to_sql("crypto_prices", engine, if_exists="append", index=False)
    print(f"Zapisano {len(df)} rekordów")

default_args = {
    "owner": "michfigg",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "crypto_daily_fetch",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2025, 12, 1),
    catchup=False,
) as dag:
    
    task = PythonOperator(
        task_id="fetch_crypto",
        python_callable=fetch_and_save_crypto,
    )