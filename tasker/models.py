from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    '''
    Stores a single task entry related to :model:`auth.User`.
    
    Fields:
    - name: The name of the task.
    - author: The User who created the task.
    - is_completed: A boolean indicating if the task is completed.
    - date_updated: The date and time when the task was last updated.
    - likes: The number of likes the task has received.
    
    Constraints:
    - Unique task name per author.
    
    Methods:
    - __str__: String representation of the model.
    '''
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasker_tasks')
    is_completed = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    
    class Meta:
        # Unique constraints to prevent:
        # - Multiple tasks with the same name from the same author.
        # - Multiple tasks with the same slug from the same author.
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'author'], name='unique_task_name_per_author'),
            models.UniqueConstraint(
                fields=['slug', 'author'], name='unique_task_slug_per_author')
        ]
        ordering = ['-date_updated']
    
    # String representation of Task model.
    def __str__(self):
        return f"TASK: {self.name} | {self.author}"


class Subtask(models.Model):
    '''
    Stores a single subtask entry related to :model:`tasker.Task`.
    
    Fields:
    - title: The title of the subtask.
    - note: Additional information about the subtask.
    - task: The Task to which the subtask belongs.
    - is_completed: A boolean indicating if the subtask is completed.
    
    Methods:
    - __str__: String representation of the model.
    '''
    title = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    is_completed = models.BooleanField(default=False)
    
    # String representation of Subtask model.
    def __str__(self):
        return f"SUBTASK: {self.title} | {self.task}"