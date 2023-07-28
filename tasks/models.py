# models.py
from django.conf import settings
from django.db import models
from django.urls import reverse


class Task(models.Model):
    CATEGORY_CHOICES = (
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('shopping', 'Shopping'),
        ('miscellaneous', 'Miscellaneous'),
    )
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='miscellaneous')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})


class CompletedTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task} - Completed on {self.date_completed}"
