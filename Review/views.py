from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Feedback.models import FeedbackData


class ListFeedbackView(LoginRequiredMixin, ListView):
    model = FeedbackData
    template_name = 'Review/list_feedback.html'
    context_object_name = 'feedbacks'
    ordering = ['-date_submitted']
    paginate_by = 10
