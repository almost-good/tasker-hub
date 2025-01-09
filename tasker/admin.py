from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task, Subtask


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    '''
    Model admin for :model:`tasker.Task`.
    '''
    readonly_fields = ('slug',) 
    list_display = (
        'name', 'slug', 'author', 'date_updated', 'likes', 'is_completed')
    list_filter = ('date_updated', 'is_completed')
    search_fields = ['name', 'author__username', 'is_completed']


# Model registration for: Subtask.
admin.site.register(Subtask)