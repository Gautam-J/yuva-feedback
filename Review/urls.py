from django.urls import path
from .views import ListFeedbackView, SearchResultsView, deleteAllFeedback

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search/', SearchResultsView.as_view(), name='SearchResultsView'),
    path('delete/', deleteAllFeedback, name='deleteAllFeedback'),
]
