from . import views
from django.urls import path


urlpatterns = [
    path('', views.BrowseTasks.as_view(), name='home'),
]
