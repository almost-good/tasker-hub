from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Task


class IndexView(generic.TemplateView):
    template_name = 'tasker/index.html'
    

class BrowseTasksView(generic.ListView):
    model = Task
    template_name = 'tasker/browse-tasks.html'
    context_object_name = 'task_list' 
    queryset = Task.objects.all()


def task_detail_view(request, username, slug):
    '''
    Display the individual :model:`tasker.Task` with the given slug and author.
    
    **Context**
    
    ``task``
        An instance of :model:`tasker.Task`.
        
    **Template:**
    
    :template:`tasker/task-detail.html`
    '''
    
    # Get the task with the given slug and author.
    queryset = Task.objects.filter(author__username=username)
    task = get_object_or_404(queryset, slug=slug)
    
    return render(
        request, 
        'tasker/task-detail.html', 
        {'task': task}
        )
    