from rest_framework import viewsets

from .models import Decision
from .serializers import DecisionSerializer


class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all().order_by('-created_at')
    serializer_class = DecisionSerializer
