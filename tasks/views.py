# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import Task, CompletedTask

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "new_task.html"
    fields = (
        "title",
        "body",
        "category",  # Assuming category field is added to the Task model
        "priority",  # Assuming priority field is added to the Task model
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
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context['object']
        completed_tasks = task.completedtask_set.all()
        context['completed_tasks'] = completed_tasks
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = (
        "title",
        "body",
        "category",
        "priority",
    )
    template_name = "task_edit.html"
    success_url = reverse_lazy('task_list')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user


class CompletedTaskListView(LoginRequiredMixin, ListView):
    model = CompletedTask
    template_name = "completed_tasks.html"
    context_object_name = "completed_tasks"  # Define the context variable name

    def get_queryset(self):
        return CompletedTask.objects.filter(task__author=self.request.user)


def mark_task_completed(request, task_id):
    task = Task.objects.get(pk=task_id)
    CompletedTask.objects.create(task=task)
    task.delete()
    return redirect('task_list')
