from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Task, Subtask, User
from .forms import TaskForm, SubtaskFormSet


class IndexView(generic.TemplateView):
    '''
    Class-based view that renders the index.html template.
    '''
    
    template_name = 'tasker/index.html'


class BrowseTasksView(LoginRequiredMixin, generic.ListView):
    '''
    Class-based view that displays a paginated list of tasks.
    '''
    
    model = Task
    template_name = 'tasker/browse-tasks.html'
    context_object_name = 'task_list' 
    queryset = Task.objects.all()
    paginate_by = 6


class YourTasksView(LoginRequiredMixin, generic.ListView):
    '''
    Class-based view that displays a list of tasks  created by the currently logged-in user.
    '''
    
    model = Task
    template_name = 'tasker/your-tasks.html'
    context_object_name = 'your_task_list' 
    paginate_by = 6
    
    def get_queryset(self):
        '''
        Returns the queryset of Task objects filtered by the current user.
        '''
        
        return Task.objects.filter(author=self.request.user)


class AddTaskView(LoginRequiredMixin, generic.CreateView):
    '''
    Class based view to handle the creation of a new task.
    '''
    
    form_class = TaskForm
    template_name = 'tasker/add-task.html'
    context_object_name = 'add_task' 

    def get_context_data(self, **kwargs):
        '''
        Override the get_context_data method to add a subtask formset to the context.
        '''
        
        context = super().get_context_data(**kwargs)
        
        if self.request.POST:
            context['subtask_formset'] = SubtaskFormSet(self.request.POST)
        else:
            context['subtask_formset'] = SubtaskFormSet()
        return context
    
    def form_valid(self, form):
        '''
        Handles the form validation and saving process for a task.
        '''
        
        form.instance.author = self.request.user
        
        name = form.cleaned_data['name']
        if Task.objects.filter(name=name, author=self.request.user).exists():
            form.add_error('name', 'A task with this name already exists. Try another.')
            context = self.get_context_data(form=form)
            return render(self.request, self.template_name, context)

        task = form.save()
        
        subtask_formset = SubtaskFormSet(self.request.POST, instance=task)
        if subtask_formset.is_valid():
            subtask_formset.save() 

        return redirect('task-detail', username=self.request.user.get_username(), slug=task.slug)


class AddSubtaskView(LoginRequiredMixin, generic.CreateView):
    '''
    View to handle the creation of a new subtask.
    '''
    
    model = Subtask
    fields = ['title', 'note', 'is_completed']
    template_name = 'tasker/add-subtask.html'
    context_object_name = 'add_subtask' 

    def form_valid(self, form):
        '''
        Handles the form validation and saving process.
        '''
        
        form.instance.author = self.request.user
        task = Task.objects.get(pk=self.kwargs['pk'])

        form.instance.task = task

        form.save()
        return redirect('task-detail', username=self.request.user.get_username(), slug=task.slug)


class EditTaskView(LoginRequiredMixin, generic.UpdateView):
    '''
    View for editing an existing task.
    '''
    
    model = Task
    form_class = TaskForm
    template_name = 'tasker/edit-task.html'
    context_object_name = 'edit_task'
    
    def get_object(self, queryset=None):
        '''
        Retrieve a Task object based on the primary key provided in the URL.
        '''
        
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return task
    
    def get_success_url(self):
        '''
        Returns the URL to redirect to after successfully handling the form.
        '''
        
        return reverse(
            'task-detail', 
            kwargs={
                'username': self.object.author.username,  # type: ignore # type: ignore 
                'slug': self.object.slug,  # type: ignore # type: ignore
            }
        )
    
    def form_valid(self, form):
        '''
        Handles the form validation process.
        '''
        
        form.instance.author = self.request.user
        name = form.cleaned_data['name']
        
        if Task.objects.filter(name=name, author=self.request.user).exists():
            form.add_error('name', 'A task with this name already exists. Try another.')
            context = self.get_context_data(form=form)
            return render(self.request, self.template_name, context)
        
        return super().form_valid(form)
    
    def get_initial(self):
        '''
        Initialize form fields with instance data.
        '''
        
        initial = super().get_initial()

        if self.object: # type: ignore # type: ignore
            initial['name'] = self.object.name # type: ignore # type: ignore
            
            if self.object.task_image:  # type: ignore
                initial['task_image'] = self.object.task_image   # type: ignore
            else:
                initial['task_image'] = ''

        return initial


class EditSubtaskView(LoginRequiredMixin, generic.UpdateView):
    '''
    View for editing an existing subtask.
    '''
    
    model = Subtask
    fields = ['title', 'note', 'is_completed']
    template_name = 'tasker/edit-subtask.html'
    context_object_name = 'edit_subtask'
    
    def get_success_url(self):
        '''
        Returns the URL to redirect to after successfully handling the form.
        '''
        
        return reverse(
            'task-detail', 
            kwargs={
                'username': self.object.task.author.username, # type: ignore
                'slug': self.object.task.slug,  # type: ignore
            }
        )


class DeleteSubtaskView(generic.DeleteView):
    '''
    View to handle the deletion of a Subtask instance.
    '''
    
    model = Subtask
    success_url = '/' 

    def get_success_url(self):
        '''
        Returns the URL to redirect to after successfully handling the form.
        '''
        
        task = self.object.task  # type: ignore
        return reverse('task-detail', kwargs={'username': task.author.username, 'slug': task.slug})


class DeleteTaskView(generic.DeleteView):
    '''
    View to handle the deletion of a Task object.
    '''
    
    model = Task
    success_url = '/' 

    def get_success_url(self):
        '''
        Returns the URL to redirect to after successfully handling the form.
        '''

        return '/your-tasks'


@login_required
def task_detail_view(request, username, slug):
    '''
    Display the individual model of :model:`tasker.Task` with the given slug.
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
    '''
    Redirects the user to the previous page they were on.
    '''
    
    return redirect(request.META.get('HTTP_REFERER', '/'))