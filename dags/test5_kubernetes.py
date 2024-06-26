# from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
# from airflow import DAG
# from airflow.configuration import conf
# from airflow.operators.bash_operator import BashOperator
# from airflow import DAG
# from datetime import datetime

# namespace = conf.get("kubernetes", "NAMESPACE")
# if namespace == "default":
#     config_file = "/usr/local/airflow/include/.kube/config"
#     in_cluster = False
# else:
#     in_cluster = True
#     config_file = None

# dag = DAG(
#     'test5',
#     default_args={'start_date': datetime(2022, 1, 1)},
#     schedule_interval='@once',
#     catchup=False
# )

# write_xcom = KubernetesPodOperator(
#     namespace="airflow2",
#     image="alpine",
#     cmds=["sh", "-c", "mkdir -p /airflow/xcom/;echo '[1,2,3,4]' > /airflow/xcom/return.json"],
#     name="test5",
#     do_xcom_push=True,
#     on_finish_action="delete_pod",
#     in_cluster=True,
#     task_id="write-xcom",
#     get_logs=True,
# )

# pod_task_xcom_result = BashOperator(
#     bash_command="echo \"{{ task_instance.xcom_pull('write-xcom')[0] }}\"",
#     task_id="pod_task_xcom_result",
# )

# write_xcom >> pod_task_xcom_result