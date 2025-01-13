import warnings

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score
import mlflow
import mlflow.sklearn
from models.train_catboost import train_cat
from data.preprocessing import load_data

warnings.filterwarnings('ignore')

import os
import sys

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

PATH = "../data/data.csv"
ITERATIONS = 100
LEARNING_RATE = 0.1
DEPTH = 6

EXPERIMENT_NAME = 'project_experiment'
# mlflow.set_tracking_uri(os.getenv("TRACKING_URI"))
mlflow.set_tracking_uri("http://host.docker.internal:5000")
mlflow.set_experiment(experiment_name=EXPERIMENT_NAME)
print(f"Current experiment: {mlflow.get_experiment_by_name(EXPERIMENT_NAME)}")

def train_model():

    X_train, X_test, y_train, y_test = load_data(PATH)
    X_test = pd.DataFrame(X_test)

    with mlflow.start_run():

        mlflow.log_param("iterations", ITERATIONS)
        mlflow.log_param("learning_rate", LEARNING_RATE)
        mlflow.log_param("depth", DEPTH)

        model = train_cat(X_train, y_train, ITERATIONS, LEARNING_RATE, DEPTH, False)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        mlflow.sklearn.log_model(model, "catboost_model_v1")
        mlflow.log_metric("accuracy_score", accuracy)
        mlflow.log_metric("best_score", model.best_score_['learn']['MultiClass'])

# инициализируем dag
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 10),
    'email_on_failure': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'train_catboost_model',
    default_args=default_args,
    catchup=False,
    description='dag для переоучения модели c применением логирования mlflow',
    schedule_interval=None,
) as dag:

    # первый таск. загрузка данных обработанных
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        op_kwargs={"path":PATH},
        provide_context=True,
    )

    # второй таск. переобучение модели
    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model, # в данном файле
        provide_context=True,
    )

    load_task >> train_task