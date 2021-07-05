from .models import Task
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView

class TaskList(ListView):
    model = Task #class based view에서 model을 models.py에서 설정한 모델이름으로 설정해주면 그 해당 모델을 이 view에서 쓸 수 있다.
    context_object_name = 'tasks' # 원래 이 views.py에서 contextobjectname을 지정해주지 않으면 html에서 objectlist로 호출해야 하는데, contextobjectname을 지정해주면 html에서 이 지정한 이름을 호출할 수 있다.

class TaskDetail(DetailView):
    model = Task