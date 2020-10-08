from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_celery_results.models import TaskResult
from celery.result import AsyncResult

from .models import Decision
from .serializers import DecisionSerializer
from .tasks import task_check_results


class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all().order_by('-created_at')
    serializer_class = DecisionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # если при сериализации объекта статус решения не перезаписан
        # то запускаем задачу celery и сразу отдаем ответ без ожидания
        if serializer.data['status'] == Decision.evaluation:
            task = task_check_results.apply_async(
                args=(serializer.data['id'],),
                kwargs={}
            )
            headers.update({'Task-Id': task.id})
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def retrieve(self, request, *args, **kwargs):
        task_id = self.request.headers.get('Task-Id', None)
        if task_id:
            try:
                TaskResult.objects.get(task_id=task_id)
            except ObjectDoesNotExist:
                # TODO: проверить по тестам это место
                res = AsyncResult(task_id)
                while res.status != 'SUCCESS':
                    res = AsyncResult(task_id)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)