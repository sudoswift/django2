from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate

app_name = 'base'

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name = 'update'),
]