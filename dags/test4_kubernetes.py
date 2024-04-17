from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow import DAG
from datetime import datetime

with DAG(
    'test4',
    default_args={'start_date': datetime(2022, 1, 1)},
    schedule_interval='@once',
    catchup=False
) as dag:

    KubernetesPodOperator(
    name="test4",
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo 10"],
    labels={"foo": "bar"},
    task_id="test4",
    do_xcom_push=True,
    in_cluster=True

)


#k.dry_run()