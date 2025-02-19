from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task, Subtask


def customize_admin_page():
    '''
    Customize the Django admin page.
    
    Sets the site header and index title for the Django admin page.
    '''
    
    admin.site.site_header = "Tasker Hub Data Administration"
    admin.site.index_title = "Tasker Hub Admin"
    admin.site.site_title = "Data Administration"


customize_admin_page()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    '''
    Registration for :model:`tasker.Task`.
    '''
    
    readonly_fields = ('slug',) 
    list_display = (
        'name', 'slug', 'author', 'date_updated', 'likes', 'is_completed')
    list_filter = ('date_updated', 'is_completed')
    search_fields = ['name', 'author__username', 'is_completed']


@admin.register(Subtask)
class SubtaskAdmin(SummernoteModelAdmin):
    '''
    Registration for :model:`tasker.Subtask`.
    '''
    
    list_display = ('task', 'title', 'note', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ['task__name', 'title', 'is_completed']
    summernote_fields = ('note',)


