from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow import DAG
from airflow.configuration import conf

namespace = conf.get("kubernetes", "NAMESPACE")
if namespace == "default":
    config_file = "/usr/local/airflow/include/.kube/config"
    in_cluster = False
else:
    in_cluster = True
    config_file = None

write_xcom = KubernetesPodOperator(
    namespace="default",
    image="alpine",
    cmds=["sh", "-c", "mkdir -p /airflow/xcom/;echo '[1,2,3,4]' > /airflow/xcom/return.json"],
    name="write-xcom",
    do_xcom_push=True,
    on_finish_action="delete_pod",
    in_cluster=True,
    task_id="write-xcom",
    get_logs=True,
)

pod_task_xcom_result = BashOperator(
    bash_command="echo \"{{ task_instance.xcom_pull('write-xcom')[0] }}\"",
    task_id="pod_task_xcom_result",
)

write_xcom >> pod_task_xcom_result