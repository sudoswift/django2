from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def rename(request):
    return HttpResponse('To Do List')
