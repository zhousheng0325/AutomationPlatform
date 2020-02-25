from celery import Celery

app = Celery("autotest")
app.config_from_object("celery_task.config")

#自动注册
app.autodiscover_tasks(['celery_task.autotask',])