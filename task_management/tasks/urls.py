# tasks/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_management, create_task, TaskDeleteView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('task_management/', task_management, name='task_management'),
    path('create/', create_task, name='create_task'),
    path('api/', include(router.urls)),
    path('api/tasks/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'), 
]
