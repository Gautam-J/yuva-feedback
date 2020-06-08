from django.urls import path
from .views import ListFeedbackView, SearchResultsView

urlpatterns = [
    path('', ListFeedbackView.as_view(), name='ListFeedbackView'),
    path('search', SearchResultsView.as_view(), name='SearchResultsView')
]
