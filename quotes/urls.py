from django.urls import path
from django.conf import settings 
from . import views

urlpatterns = [
    path(r'', views.quote, name="quote"), # our first url
    path(r'about', views.about, name="about"), # our first url
    path(r'show_all', views.show_all, name="show_all"), # our first url
]