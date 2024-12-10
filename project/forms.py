# Kyle Yung, yungk@bu.edu
# creates from classes used to create, delete and update various models in the application
#project/forms.py

from django import forms
from .models import *

class CreateProfileForm(forms.ModelForm):
        '''A form to create profile data.'''

        class Meta:
                '''associate this form with the Profile model'''
                model = Profile
                fields = ['first_name', 'last_name', 'email', 'image_url',]

class CreateProductForm(forms.ModelForm):
        '''A form to create product data.'''

        class Meta:
                '''associate this form with the Product model'''
                model = Product
                fields = ['title', 'description', 'price', 'image_url',]

class CreateReviewForm(forms.ModelForm):
        '''A form to create review data.'''

        class Meta:
                '''associate this form with the review model'''
                model = Review
                fields = ['message']

class UpdateProfileForm(forms.ModelForm):
        '''A form to update profile data.'''
        class Meta:
                '''associate this form with the profile model'''
                model = Profile
                fields = ['first_name', 'last_name', 'email', 'image_url',]

class UpdateProductForm(forms.ModelForm):
        '''A form to update product data.'''
        class Meta:
                '''associate this form with the product model'''
                model = Product
                fields = ['title', 'description', 'price', 'image_url',]

class UpdateReviewForm(forms.ModelForm):
        '''A form to update review data.'''
        class Meta:
                '''associate this form with the review model'''
                model = Review
                fields = ['message',]

class AddOrderForm(forms.ModelForm):
        '''A form to add orderitem data.'''
        class Meta:
                '''associate this form with the OrderItem model'''
                model = OrderItem
                fields = ['quantity',]

class UpdateOrderItemForm(forms.ModelForm):
        '''A form to update orderitem data.'''
        class Meta:
                '''associate this form with the orderitem model'''
                model = OrderItem
                fields = ['quantity',]

                