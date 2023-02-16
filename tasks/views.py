from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "new_task.html"
    fields = (
        "title",
        "body",
    )
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = (
        "title",
        "body",
    )
    template_name = "task_edit.html"
    success_url = reverse_lazy('task_list')

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user

