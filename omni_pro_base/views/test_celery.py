from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from omni_pro_base.tasks.task_test_celery import TaskTestCelery


class TestCelery(ViewSet):

    permission_classes = []

    def test_celerity_task(self, request):
        """
        {
            "num1": 1,
            "num2": 2
        }
        """
        try:
            data = request.data
            num1 = data.get('num1', 0)
            num2 = data.get('num2', 0)

            result = TaskTestCelery.task_test_celery.delay(num1, num2)

        except Exception as exc:
            print('Failed')

        return Response({"mensaje": "Ok"}, status=status.HTTP_201_CREATED)
