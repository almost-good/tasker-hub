from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task, Subtask, User
from .forms import TaskForm, SubtaskFormSet


class IndexView(generic.TemplateView):
    template_name = 'tasker/index.html'


class BrowseTasksView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasker/browse-tasks.html'
    context_object_name = 'task_list' 
    queryset = Task.objects.all()
    paginate_by = 6


class YourTasksView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasker/your-tasks.html'
    context_object_name = 'your_task_list' 
    paginate_by = 6
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class AddTaskView(LoginRequiredMixin, generic.CreateView):
    form_class = TaskForm
    template_name = 'tasker/add-task.html'
    context_object_name = 'add_task' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['subtask_formset'] = SubtaskFormSet(self.request.POST)
        else:
            context['subtask_formset'] = SubtaskFormSet()
        return context
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        task = form.save()
        
        subtask_formset = SubtaskFormSet(self.request.POST, instance=task)
        if subtask_formset.is_valid():
            subtask_formset.save() 

        return redirect('task-detail', username=self.request.user.get_username(), slug=task.slug)



@login_required
def task_detail_view(request, username, slug):
    '''
    Display the individual model of :model:`tasker.Task` with the given slug.
    
    **Context:**
    
    ``task``
        The task with the given slug.
    ``subtasks``
        All the subtasks related to the task.
        
    **Template:**

    :template:`tasker/task-detail.html`
    '''
    
    # Get the task with the given slug and author.
    queryset = Task.objects.filter(author__username=username)
    task = get_object_or_404(queryset, slug=slug)
    
    # Get all the subtasks related to the task.
    subtasks = task.subtasks.all()
    
    return render(
        request, 
        'tasker/task-detail.html', 
        {
            'task': task, 
            'subtasks': subtasks
        }
    )

def go_back_view(request):
    return redirect(request.META.get('HTTP_REFERER', '/'))