from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class TaskPageView(TemplateView):
    template_name = "task_list.html"
