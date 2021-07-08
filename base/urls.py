from django.urls import path
from .views import TaskDelete, TaskList, TaskDetail, TaskCreate, TaskUpdate, CustomLoginView
from django.contrib.auth.views import LogoutView #로그아웃 뷰는 views.py에 별도로 설정할 필요 없이 urls.py에서 설정해주면 된다.

app_name = 'base'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'base:login'), name = 'logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name = 'delete'),
]