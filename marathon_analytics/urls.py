# marathon_analytics/urls.py

from django.urls import path
from . import views
urlpatterns = [
    # map the URL to the view
    path('', views.ResultsListView.as_view(), name='home'),
    path('results', views.ResultsListView.as_view(), name='results'),
]