#mini_fb/views.py
# views to show the mini facebook app

from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from . models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_context_data(self, **kwargs: Any):
        '''
        provides context data to the template.
        '''

        context = super().get_context_data(**kwargs)
        context['form2'] = UserCreationForm(self.request.POST)
        return context
    
    def form_valid(self, form):
        '''this method executes after form submission'''

        form2 = UserCreationForm(self.request.POST)
        # if not valid, let super class handle
        if not form2.is_valid():
            return super().form_invalid(form2)
        # if it is, save it to database
        pv = form2.save()
        # attach instance to profile
        profile = form.instance
        profile.user = pv
        profile.save()
        login(self.request, pv)
        return redirect('show_profile', pk=profile.pk)

class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    '''a view to show/process the create status message form
    on GET: send back the form
    on POST: read the form data, create an instant of a status message; save to database;'''
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    #what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse('show_profile', kwargs={'pk': self.object.profile.pk})

    def form_valid(self, form):
        '''this method executes after form submission'''

        #find the profile with the PK from the URL
        profile = self.get_object()

        # attach the profile to the status message
        # (form.instance is the new status message object)
        form.instance.profile = profile
        # save the status message to database
        sm = form.save()

        files = self.request.FILES.getlist('files')

        for file in files:
            img = Image(status_message = sm, image_file = file)
            img.save()

        # deleguate work to the superclass version of this method
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''build the template context data -- a dict of key-value pairs'''
        context = super().get_context_data(**kwargs)

        profile = self.get_object()

        context['profile'] = profile

        return context

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self) -> str:
        user = Profile.objects.get(user=self.request.user)
        return user

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''a view to show/process the update profile form
    on GET: send back the form
    on POST: read the form data, update the instant of a profile; save to database;'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self) -> str:
        user = Profile.objects.get(user=self.request.user)
        return user

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    '''a view to show/process the deletion of a status message'''
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'status'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse("show_profile", kwargs={'pk': self.object.profile.pk})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    '''a view to show/process the update of a status message'''
    model = StatusMessage
    form_class = UpdateStatusForm
    template_name = 'mini_fb/update_status_form.html'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful update'''
        return reverse("show_profile", kwargs={'pk': self.object.profile.pk})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class CreateFriendView(LoginRequiredMixin, View):
    '''
    class-based view called CreateFriendView, which inherits from the generic View class.
    '''
    def dispatch(self, request, other_pk):
        '''
        read the URL parameters (from self.kwargs), use the object manager to find the requisite Profile objects, and then call the Profile's add_friend method.
        '''
        p1 = self.get_object()
        p2 = Profile.objects.get(pk=other_pk)
        p1.add_friend(p2)
        return redirect('show_profile', pk=p1.pk)
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self) -> str:
        user = Profile.objects.get(user=self.request.user)
        return user

class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
    '''a view to show friend suggestions'''
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self) -> str:
        user = Profile.objects.get(user=self.request.user)
        return user

class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    '''a view to show the news feed'''
    model = Profile
    template_name = 'mini_fb/news_feed.html'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_object(self) -> str:
        user = Profile.objects.get(user=self.request.user)
        return user