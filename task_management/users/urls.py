from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth import views as auth_views

from .views import (
    UserRegisterView,
    CustomTokenObtainPairView,
    LogoutView,
    admin_dashboard,
    manager_dashboard,
    user_dashboard,
    user_management,
    login_page,
    register_page,
    task_management,
    create_task,
)

urlpatterns = [
    path('api/register/', UserRegisterView.as_view(), name='api_register'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='api_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),

    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/manager/', manager_dashboard, name='manager_dashboard'),
    path('dashboard/user/', user_dashboard, name='user_dashboard'),
    path('user_management/', user_management, name='user_management'),

    path('login/', login_page, name='login_page'), 
    path('register/', register_page, name='register_page'),
    path('tasks/', task_management, name='task_management'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', create_task, name='create_task'),
]
