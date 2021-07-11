from .models import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # 로그인을 하지 않은 회원에게 특정 뷰를 보여주고 싶지 않다면 다음 loginrequiredmixin을 import 해준 후 해당 뷰의 class의 파라미터에 loginrequiredmixin을 넣어준다.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
     template_name = 'base/login.html'
     fields = '__all__'
     def get_success_url(self):
        return reverse_lazy('base:tasks')
     redirect_authenticated_user = True #이미 로그인이 돼 authenticated된 유저의 경우 로그인페이지에 접근하지 못하게 한다. 기본값이 False 이므로 꼭 true로 변경해줘야 한다.

class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('base:tasks')
    def form_valid(self, form): #회원가입이 성공적으로 작동했다면 자동으로 로그인되게 하는 함수
        user = form.save() 
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base:tasks')
        return super(RegisterView, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task #class based view에서 model을 models.py에서 설정한 모델이름으로 설정해주면 그 해당 모델을 이 view에서 쓸 수 있다.
    context_object_name = 'tasks' # 원래 이 views.py에서 contextobjectname을 지정해주지 않으면 html에서 objectlist로 호출해야 하는데, contextobjectname을 지정해주면 html에서 이 지정한 이름을 호출할 수 있다.
    template_name = 'base/tasks.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        lookingfor = self.request.GET.get('lookingfor') or ''
        if lookingfor:
            context['tasks'] = context['tasks'].filter(title__icontains = lookingfor)

        context['lookingfor'] = lookingfor
        return context

    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:tasks') #석세스유알엘은 특정 행동을 한 후 어떤 페이지로 이동할 것인지 지정해주는 속성이다. reverse와 reverselazy 함수는 urls.py에서 appname을 지정해줘야 사용할 수 있다. 이 name을 지정하면 urls.py가 자동으로 해당 url로 매핑해준다. view의 generic을 사용할때는 reverse가 아닌 reverselazy를 사용해야한다. 경로를 appname까지 정확하게 맞춰줘야 reverselazy가 작동한다.
    template_name = 'base/create.html'
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('base:tasks')
    template_name = 'base/create.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('base:tasks')
    template_name = 'base/delete.html'
