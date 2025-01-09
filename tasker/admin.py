from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Task, Subtask


# Model registration for: Task.
@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('name',)
    readonly_fields = ('slug',) 


# Model registration for: Subtask.
admin.site.register(Subtask)