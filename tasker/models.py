from django.db import models
from django.db.models.query import QuerySet
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Task(models.Model):
    '''
    Stores a single task entry related to :model:`auth.User`.
    '''
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=200, unique=False, blank=True, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasker_tasks')
    task_image = CloudinaryField('image', default='placeholder')
    is_completed = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    # Tell linter that `subtasks` is a QuerySet of Subtask objects
    subtasks: QuerySet["Subtask"]  

    def save(self, *args, **kwargs):
        '''
        Overriding the save method to automatically generate a slug for the task.
        
        The slug is generated by converting the task name to a slug and appending 
        a number to the slug if a task with the same slug already exists.
        '''
        
        current_slug = slugify(self.name)
        unique_slug = current_slug
        num = 1
        
        # Check if a task with the same slug already exists, excluding the current task.
        while (
            Task.objects.filter(slug=unique_slug, author=self.author)
            .exclude(pk=self.pk)
            .exists()
            ):
            unique_slug = f"{current_slug}-{num}"
            num += 1
        
        self.slug = unique_slug
        super().save(*args, **kwargs)
    
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
    
    def __str__(self):

        return f"TASK: {self.name} | {self.author}"


class Subtask(models.Model):
    '''
    Stores a single subtask entry related to :model:`tasker.Task`.
    '''
    
    title = models.CharField(max_length=200)
    note = models.TextField(blank=True)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='subtasks')
    is_completed = models.BooleanField(default=False)
    
    # String representation of Subtask model.
    def __str__(self):
        return f"SUBTASK: {self.title} | {self.task}"