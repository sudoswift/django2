from django.urls import path
from .views import TaskList

app_name = 'base'

urlpatterns = [
    path('', TaskList.as_view(), name='tasks')
]