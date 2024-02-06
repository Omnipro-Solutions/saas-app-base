
from time import sleep
from omni_pro_base.setting import CELERY_MAX_RETRIES, CELERY_SECONDS_TIME_TO_RETRY
from celery import shared_task, current_task, Celery


class TaskTestCelery:

    @staticmethod
    @shared_task(name='omni_pro_base.tasks.task_test_celery')
    def task_test_celery(x, y):
        try:
            sleep(2)
            return x + y

        except Exception as exc:
            print(f"Tarea fallida: {exc}")
            raise current_task.retry(exc=exc, countdown=2)
