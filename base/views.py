from .models import Task
from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic.list import ListView

class TaskList(ListView):
    model = Task