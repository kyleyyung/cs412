# marathon_analytics/urls.py

from django.urls import path
from . import views
urlpatterns = [
    # map the URL to the view
    path(r'', views.ResultsListView.as_view(), name='home'),
    path(r'results', views.ResultsListView.as_view(), name='results'),
    path(r'voter/<int:pk>', views.VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphsView.as_view(), name='graphs'),
]