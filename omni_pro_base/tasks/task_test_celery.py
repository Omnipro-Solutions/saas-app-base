
from time import sleep
from celery import shared_task, current_task, Celery


class TaskTestCelery:

    @staticmethod
    @shared_task
    def task_test_celery(x, y):
        try:
            sleep(2)
            return x + y

        except Exception as exc:
            print(f"Tarea fallida: {exc}")
            raise current_task.retry(exc=exc, countdown=2)
