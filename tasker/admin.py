from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task, Subtask


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    '''
    Registration for :model:`tasker.Task`.
    '''
    readonly_fields = ('slug',) 
    list_display = (
        'name', 'slug', 'author', 'date_updated', 'likes', 'is_completed')
    list_filter = ('date_updated', 'is_completed')
    search_fields = ['name', 'author__username', 'is_completed']


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    '''
    Registration for :model:`tasker.Subtask`.
    '''
    list_display = ('task', 'title', 'note', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ['task__name', 'title', 'is_completed']
    summernote_fields = ('note',)


