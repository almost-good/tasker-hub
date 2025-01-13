from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('browse-tasks', views.BrowseTasksView.as_view(), name='browse-tasks'),
    path('tasker/<str:username>/<slug:slug>/', views.task_detail_view, name='task-detail'),
    path('your-tasks', views.YourTasksView.as_view(), name='your-tasks'),
]
