# import kubernetes.client as k8s
# from airflow import DAG
# from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
# # from airflow.providers.cncf.kubernetes.callbacks import KubernetesPodOperatorCallback
# from datetime import datetime

# class MyCallback(KubernetesPodOperatorCallback):
#     @staticmethod
#     def on_pod_creation(*, pod: k8s.V1Pod, client: k8s.CoreV1Api, mode: str, **kwargs) -> None:
#         client.create_namespaced_service(
#             namespace=pod.metadata.namespace,
#             body=k8s.V1Service(
#                 metadata=k8s.V1ObjectMeta(
#                     name=pod.metadata.name,
#                     labels=pod.metadata.labels,
#                     owner_references=[
#                         k8s.V1OwnerReference(
#                             api_version=pod.api_version,
#                             kind=pod.kind,
#                             name=pod.metadata.name,
#                             uid=pod.metadata.uid,
#                             controller=True,
#                             block_owner_deletion=True,
#                         )
#                     ],
#                 ),
#                 spec=k8s.V1ServiceSpec(
#                     selector=pod.metadata.labels,
#                     ports=[
#                         k8s.V1ServicePort(
#                             name="http",
#                             port=80,
#                             target_port=80,
#                         )
#                     ],
#                 ),
#             ),
#         )

# dag = DAG(
#     'test3',
#     default_args={'start_date': datetime(2022, 1, 1)},
#     schedule_interval='@once',
#     catchup=False
# )

# k = KubernetesPodOperator(
#     task_id="test3_kube",
#     image="alpine",
#     cmds=["/bin/sh"],
#     arguments=["-c", "echo hello world; echo Custom error > /dev/termination-log; exit 1;"],
#     name="test3_kube"
# )