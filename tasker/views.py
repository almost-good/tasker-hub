from django.shortcuts import render
from django.views import generic
from .models import Task


class IndexView(generic.TemplateView):
    template_name = 'tasker/index.html'
    

class BrowseTasksView(generic.ListView):
    model = Task
    template_name = 'tasker/browse-tasks.html'
    queryset = Task.objects.all()

