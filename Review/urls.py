from django.urls import path
from .views import ListFeedbackView

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
]
