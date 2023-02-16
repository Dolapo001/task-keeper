from django.urls import path

from .views import HomePageView, TaskPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('tasks/', TaskPageView.as_view, name="tasks")
]
