from rest_framework import viewsets, permissions
from .serializers import TaskSerializer
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['completed']
    permission_classes = [permissions.IsAuthenticated]

