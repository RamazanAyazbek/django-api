from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permissions_classes=[
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer