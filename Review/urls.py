from django.urls import path
from .views import LoginView, ListFeedbackView

urlpatterns = [
    path('', LoginView.as_view(), name='LoginView'),
    path('list_feedback', ListFeedbackView.as_view(), name='ListFeedbackView'),
]
