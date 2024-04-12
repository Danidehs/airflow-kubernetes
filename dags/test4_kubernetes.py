from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

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