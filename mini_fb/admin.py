from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Profile) # registers a section called Profile in the admin page
admin.site.register(StatusMessage) # registers a section called StatusMessage in the admin page
