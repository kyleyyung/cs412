#mini_fb/forms.py

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
        '''A form to create profile data.'''

        class Meta:
                '''associate this form with the Profile model'''
                model = Profile
                fields = ['first_name', 'last_name', 'city', 'email', 'image_url',]

class CreateStatusMessageForm(forms.ModelForm):
        '''A form to create status message data.'''

        class Meta:
                '''associate this form with the status message model'''
                model = StatusMessage
                fields = ['message']

                