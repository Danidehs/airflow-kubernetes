from pendulum import datetime, duration
from airflow import DAG
from airflow.configuration import conf
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": duration(minutes=5),
}

namespace = conf.get("kubernetes", "NAMESPACE")
# This will detect the default namespace locally and read the
# environment namespace when deployed to Astronomer.
if namespace == "default":
    config_file = "/usr/local/airflow/include/.kube/config"
    in_cluster = False
else:
    in_cluster = True
    config_file = None

with DAG(
    dag_id="example_kubernetes_pod", schedule="@once"
) as dag:
    KubernetesPodOperator(
        # config_file="/home/airflow/composer_kube_config",
        namespace="airflow2",
        image="airflow-cluster",
        name="airflow-test-pod",
        task_id="task-one",
        #in_cluster=in_cluster,  # if set to true, will look in the cluster, if false, looks for file
        # cluster_context="docker-desktop",  # is ignored when in_cluster is set to True
        #config_file=config_file,
        is_delete_operator_pod=True,
        get_logs=True,
        in_cluster=True,
    )