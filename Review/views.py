from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListFeedbackView(LoginRequiredMixin, TemplateView):
    template_name = 'Review/list_feedback.html'
