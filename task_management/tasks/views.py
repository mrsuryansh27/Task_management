# tasks/views.py

from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from users.permissions import IsAdminUser, IsManagerUser, IsRegularUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import TaskForm 
from rest_framework import generics, permissions

@login_required
def task_management(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'task_management.html', context)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.request.user.role == 'admin':
            permission_classes = [IsAdminUser]
        elif self.request.user.role == 'manager':
            permission_classes = [IsManagerUser]
        else:
            permission_classes = [IsRegularUser]
        return [permission() for permission in permission_classes]

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user  
            task.save()  

            return JsonResponse({'message': 'Task created successfully.'})
        else:
            return JsonResponse({'error': 'Form validation error.'}, status=400)
    else:
        form = TaskForm()  
    return render(request, 'create_task.html', {'form': form})



class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        if task.owner != request.user:
            return Response({'error': 'You do not have permission to delete this task.'}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, *args, **kwargs)
