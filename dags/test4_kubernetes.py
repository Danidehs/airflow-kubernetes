from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow import DAG
from datetime import datetime

dag = DAG(
    'test4',
    default_args={'start_date': datetime(2022, 1, 1)},
    schedule_interval='@once',
    catchup=False
)

k = KubernetesPodOperator(
    name="dry_run_test_k8s",
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo 10"],
    labels={"foo": "bar"},
    task_id="dry_run_demo",
    do_xcom_push=True,
    in_cluster=True

)


k.dry_run()