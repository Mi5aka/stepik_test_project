from rest_framework import viewsets, status
from rest_framework.response import Response
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from djangochannelsrestframework.observer import model_observer

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
        task_check_results.apply_async(args=(serializer.data['id'],), kwargs={})
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

'''
class LiveDecisionConsumer(
    PatchModelMixin,
    GenericAsyncAPIConsumer
):

    queryset = Decision.objects.all()
    serializer_class = DecisionSerializer
    permission_classes = (permissions.AllowAny,)

    @model_observer(Decision)
    async def post_change_handler(self, message, observer=None, **kwargs):
        # called when a subscribed item changes
        print('Я работаю!')
        await self.send_json(message)
'''