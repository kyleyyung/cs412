#blog/forms.py

from django import forms
from .models import *

class CreateCommentForm(forms.ModelForm):
        '''A form to create Comment data.'''

        class Meta:
                '''associate this form with the Comment model'''
                model = Comment

                fields = ['author', 'text',]

class CreateArticleForm(forms.ModelForm):
    '''A form to add a new Article to the database.'''
    class Meta:
        '''Associate this form with the Article model; select fields to add.'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']
                