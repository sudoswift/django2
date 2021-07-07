from .models import Task
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class TaskList(ListView):
    model = Task #class based view에서 model을 models.py에서 설정한 모델이름으로 설정해주면 그 해당 모델을 이 view에서 쓸 수 있다.
    context_object_name = 'tasks' # 원래 이 views.py에서 contextobjectname을 지정해주지 않으면 html에서 objectlist로 호출해야 하는데, contextobjectname을 지정해주면 html에서 이 지정한 이름을 호출할 수 있다.
    template_name = 'base/tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:tasks') #석세스유알엘은 특정 행동을 한 후 어떤 페이지로 이동할 것인지 지정해주는 속성이다. reverse와 reverselazy 함수는 urls.py에서 appname을 지정해줘야 사용할 수 있다. 이 name을 지정하면 urls.py가 자동으로 해당 url로 매핑해준다. view의 generic을 사용할때는 reverse가 아닌 reverselazy를 사용해야한다. 경로를 appname까지 정확하게 맞춰줘야 reverselazy가 작동한다.
    template_name = 'base/create.html'

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('base:tasks')