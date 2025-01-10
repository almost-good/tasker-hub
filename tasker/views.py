from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Task


class BrowseTasks(generic.ListView):
    model = Task
    template_name = 'tasker/index.html'
    queryset = Task.objects.all()
