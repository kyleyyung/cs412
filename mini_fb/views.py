#mini_fb/views.py
# views to show the mini facebook app

from django.shortcuts import render
from . models import *
from django.views.generic import ListView

class ShowAllProfilesView(ListView):
    '''A view to show all Profiles'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'