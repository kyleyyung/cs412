#mini_fb/views.py
# views to show the mini facebook app

from typing import Any
from django.shortcuts import render
from django.urls import reverse
from . models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView

class ShowAllProfilesView(ListView):
    '''A view to show all Profiles'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    '''A view to show all Profiles'''

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    '''a view to show/process the create profile form
    on GET: send back the form
    on POST: read the form data, create an instant of profile; save to database;'''
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        #return "/mini_fb/show_all"
        # return reverse("show_all")
        return self.object.get_absolute_url()
    
class CreateStatusMessageView(CreateView):
    '''a view to show/process the create status message form
    on GET: send back the form
    on POST: read the form data, create an instant of a status message; save to database;'''
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    #what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse("show_profile", kwargs=self.kwargs)

    def form_valid(self, form):
        '''this method executes after form submission'''

        #find the profile with the PK from the URL
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        # attach the profile to the status message
        # (form.instance is the new status message object)
        form.instance.profile = profile

        # deleguate work to the superclass version of this method
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''bild the template context data -- a dict of key-value pairs'''
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(pk=self.kwargs['pk'])

        context['profile'] = profile

        return context