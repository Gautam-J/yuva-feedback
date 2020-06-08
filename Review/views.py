from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'Review/login.html'


class ListFeedbackView(TemplateView):
    template_name = 'Review/list_feedback.html'
