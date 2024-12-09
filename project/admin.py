from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Profile) # registers a section called User in the admin page
admin.site.register(Product) # registers a section called Product in the admin page
admin.site.register(Review) # registers a section called Review in the admin page
admin.site.register(Order) # registers a section called Order in the admin page
admin.site.register(OrderItem) # registers a section called OrderItem in the admin page