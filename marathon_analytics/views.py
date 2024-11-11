from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import Result
from typing import Any

# Create your views here.

class ResultsListView(ListView):
    '''View to display marathon results'''
    template_name = 'marathon_analytics/results.html'
    model = Result
    context_object_name = 'results'
    paginate_by = 50
    
    def get_queryset(self):
        '''return the set of Results'''

        #use the superclass version of query set
        qs = super().get_queryset()
        #return qs[:25]

        # if we have a search parameter, use it to filter the query set
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city: # not empty string
                qs = Result.objects.filter(city__icontains = city)
        return qs