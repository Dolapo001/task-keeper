from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import Task


class TaskCreateView(CreateView):
    model = Task
    template_name = "new_task.html"
    fields = (
        "title",
        "body",
        "author",
    )


class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"


class TaskDetailView(DetailView): # new
    model = Task
    template_name = "task_detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = (
        "title",
        "body",
    )
    template_name = "task_edit.html"


class TaskDeleteView(DeleteView): # new
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")
