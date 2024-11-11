from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Voter
from typing import Any
from datetime import datetime
from functools import reduce
import plotly
import plotly.graph_objects as go

# Create your views here.

class ResultsListView(ListView):
    '''View to display marathon results'''
    template_name = 'voter_analytics/results.html'
    model = Voter
    context_object_name = 'results'
    paginate_by = 100

    def get_queryset(self):
        '''return the set of Results'''

        #use the superclass version of query set
        qs = super().get_queryset()

        # if we have a search parameter, use it to filter the query set
        if 'party' in self.request.GET and self.request.GET['party'] != 'all':
            party = self.request.GET['party']
            if party: # not empty string
                qs = Voter.objects.filter(party__icontains = party)
        if 'min_dob' in self.request.GET and self.request.GET['min_dob'] != 'all':
            min_dob = self.request.GET['min_dob']
            # return voters who's birth year is greater than or equal to min_dob
            if min_dob: # if not empty
                qs = Voter.objects.filter(dob__year__gte=min_dob)
        if 'max_dob' in self.request.GET and self.request.GET['max_dob'] != 'all':
            max_dob = self.request.GET['max_dob']
            # return voters who's birth year is less than or equal to max_dob
            if max_dob: # if not empty
                qs = Voter.objects.filter(dob__year__lte=max_dob)
        # for searches that have both min_dob and max_dob
        if 'min_dob' in self.request.GET and 'max_dob' in self.request.GET and self.request.GET['min_dob'] != 'all' and self.request.GET['max_dob'] != 'all':
            min_dob = self.request.GET['min_dob']
            max_dob = self.request.GET['max_dob']
            if min_dob and max_dob: # if not empty
                qs = Voter.objects.filter(dob__year__gte=min_dob, dob__year__lte=max_dob)
        if 'score' in self.request.GET and self.request.GET['score'] != 'all':
            score = self.request.GET['score']
            if score: # not empty string
                qs = Voter.objects.filter(score__icontains = score)
        if 'v20state' in self.request.GET and self.request.GET['v20state']:
            qs = qs.filter(v20state__icontains="TRUE")
        if 'v21town' in self.request.GET and self.request.GET['v21town']:
            qs = qs.filter(v21town__icontains="TRUE")
        if 'v21primary' in self.request.GET and self.request.GET['v21primary']:
            qs = qs.filter(v21primary__icontains="TRUE")
        if 'v22general' in self.request.GET and self.request.GET['v22general']:
            qs = qs.filter(v22general__icontains="TRUE")
        if 'v23town' in self.request.GET and self.request.GET['v23town']:
            qs = qs.filter(v23town__icontains="TRUE")
        return qs
    
class VoterDetailView(DetailView):
    '''Show the details for one Voter'''
    model = Voter
    template_name = 'voter_analytics/voter_detail.html'
    context_object_name = 'voter'

    def get_context_data(self, **kwargs):
        ''' Add some data to the context object. '''
        context = super().get_context_data(**kwargs)
        r = context['voter']
        return context

class GraphsView(ListView):
    ''' View to display list of graphs. '''

    template_name = 'voter_analytics/graphs.html'
    model = Voter
    context_object_name = 'voters'

    def get_queryset(self):
        '''Party affiliation (drop-down list)
            Minimum date of birth (a drop-down list by calendar year)

            Maximum date of birth (a drop-down list by calendar year)

            Voter Score (a drop-down list)

            Whether they voted in specific elections (check boxes)

            The search should be able to accurately filter any selection of criteria, and none of the filters are required. For example, it should be possible to find voters who are born after 1975 but before 2000, who have a voter score of 4 (but without specifying their party affiliation or specific elections).
        '''
        # use the superclass version of the queryset
        qs = super().get_queryset()

        # if they select all, act like there is no input for that field
        if 'party_affiliation' in self.request.GET and self.request.GET['party_affiliation'] != 'all':
            party_affiliation = self.request.GET['party_affiliation']
            if party_affiliation: # if not empty
                qs = Voter.objects.filter(party_affiliation__icontains=party_affiliation)
        if 'min_dob' in self.request.GET and self.request.GET['min_dob'] != 'all':
            min_dob = self.request.GET['min_dob']
            # returns voters whos birth year is greater than or equal to min_dob
            if min_dob: # if not empty
                qs = Voter.objects.filter(dob__year__gte=min_dob)
        if 'max_dob' in self.request.GET and self.request.GET['max_dob'] != 'all':
            max_dob = self.request.GET['max_dob']
            # returns voters whos birth year is less than or equal to max_dob
            if max_dob: # if not empty
                qs = Voter.objects.filter(dob__year__lte=max_dob)
        # for searches that have both min_dob and max_dob
        if 'min_dob' in self.request.GET and 'max_dob' in self.request.GET and self.request.GET['min_dob'] != 'all' and self.request.GET['max_dob'] != 'all':
            min_dob = self.request.GET['min_dob']
            max_dob = self.request.GET['max_dob']
            if min_dob and max_dob: # if not empty
                qs = Voter.objects.filter(dob__year__gte=min_dob, dob__year__lte=max_dob)
        if 'voter_score' in self.request.GET and self.request.GET['voter_score'] != 'all':
            voter_score = self.request.GET['voter_score']
            if voter_score: # if not empty
                qs = Voter.objects.filter(voter_score__icontains=voter_score)
        if 'v20state' in self.request.GET and self.request.GET['v20state']:
            qs = qs.filter(v20state__icontains="TRUE")
        if 'v21town' in self.request.GET and self.request.GET['v21town']:
            qs = qs.filter(v21town__icontains="TRUE")
        if 'v21primary' in self.request.GET and self.request.GET['v21primary']:
            qs = qs.filter(v21primary__icontains="TRUE")
        if 'v22general' in self.request.GET and self.request.GET['v22general']:
            qs = qs.filter(v22general__icontains="TRUE")
        if 'v23town' in self.request.GET and self.request.GET['v23town']:
            qs = qs.filter(v23town__icontains="TRUE")
        return qs

    def get_context_data(self, **kwargs):
        '''
        Add some data to the context object, including graphs.
        '''
        context = super().get_context_data(**kwargs)

        ## Histogram displaying voter distribution by year of birth.
        x = []
        y = []
        for voter in self.object_list:
            year = voter.dob.year
            if year not in x:
                x.append(year)
                y.append(1)
            else:
                y[x.index(year)] += 1

        num = sum(y)
        fig = go.Figure(data=[go.Bar(x=x, y=y)])

        # Display title with sample size included
        fig.update_layout(
            title=f"Voter Distribution by Year of Birth (n={num})",
        )

        graph_bar = plotly.offline.plot(fig, auto_open=False, output_type='div')

        # add graph to context
        context['graph_bar'] = graph_bar

        ## Create pie chart dispalying the distribution of Voters by party affiliation.
        x = []
        y = []
        for voter in self.object_list:
            if voter.party not in x:
                x.append(voter.party)
                y.append(1)
            else:
                y[x.index(voter.party)] += 1

        # Create pie chart figure
        fig = go.Figure(data=[go.Pie(labels=x, values=y)])

        # Display title with sample size included
        fig.update_layout(
            title=f"Voter Distribution by Party Affiliation (n = {num})"
        )

        graph_pie = plotly.offline.plot(fig, auto_open=False, output_type='div')

        # add graph to context
        context['graph_pie'] = graph_pie

        ## A histogram displaying the vote count by elections.
        # voter will iterate through each voter and keep a counter for each election
        x = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        y = [0, 0, 0, 0, 0]
        for voter in self.object_list:
            if voter.v20state == "TRUE":
                y[0] += 1
            if voter.v21town == "TRUE":
                y[1] += 1
            if voter.v21primary == "TRUE":
                y[2] += 1
            if voter.v22general == "TRUE":
                y[3] += 1
            if voter.v23town == "TRUE":
                y[4] += 1

        fig = go.Figure(data=[go.Bar(x=x, y=y)])

        # Display title with sample size included
        fig.update_layout(
            title=f"Vote Count by Election (n={num})",
        )

        graph_bar2 = plotly.offline.plot(fig, auto_open=False, output_type='div')

        # add the graph to the context
        context['graph_bar2'] = graph_bar2
        return context