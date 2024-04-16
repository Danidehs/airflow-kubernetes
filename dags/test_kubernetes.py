import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from kubernetes.client.models import V1EnvVar

with DAG('test_kubernetes',
         schedule_interval='@once',
         start_date=datetime(2022, 1, 1),
         catchup=False) as dag:


    task = KubernetesPodOperator(
        namespace='airflow2',
        # config_file="/home/airflow/composer_kube_config",
        image='python:3.11',
        cmds=["python", "-c"],
        arguments=["print('Hello from the Kubernetes Pod!')"],
        labels={"foo": "bar"},
        name="airflow-test-pod",
        task_id="task",
        get_logs=True,
        in_cluster=True,
    )
