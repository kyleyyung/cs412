#define data models (objects) for use in the mini facebook application
from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''Encapsulates the data for a Profile'''

    # data attributes
    first_name= models.TextField(blank = False)
    last_name = models.TextField(blank = False)
    city = models.TextField(blank = False)
    email = models.TextField(blank = False)
    image_url = models.URLField(blank = True)

    def __str__(self):
        '''Return a string representation of this Profile'''
        return f"{self.first_name} {self.last_name}"

    def get_status_messages(self):
        '''Retrieve all status Mmssages for this Profile'''

        # use the ORM to filter status messages where this instance of Profile is the foreign key
        status_messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp')
        return status_messages
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse("show_profile", kwargs={'pk': self.pk})

class StatusMessage(models.Model):
    timestamp = models.DateTimeField(auto_now = True)
    message = models.TextField(blank = False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def get_images(self):
        # use the ORM to filter images where this instance of status message is the foreign key
        images = Image.objects.filter(status_message=self)
        return images
    
    def __str__(self):
        '''Return a string representation of this Status Message'''
        return f"{self.message}"
    
class Image(models.Model):
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now = True)
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)