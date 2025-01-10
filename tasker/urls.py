from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('browse-tasks', views.BrowseTasksView.as_view(), name='browse-tasks'),
]
