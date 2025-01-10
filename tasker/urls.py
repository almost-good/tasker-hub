from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('', views.BrowseTasksView.as_view(), name='browse-tasks'),
]
