#define data models (objects) for use in the mini facebook application
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''Encapsulates the data for a Profile'''

    # data attributes
    first_name= models.TextField(blank = False)
    last_name = models.TextField(blank = False)
    city = models.TextField(blank = False)
    email = models.TextField(blank = False)
    image_url = models.URLField(blank = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mini_fb_profile')

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
    
    def get_friends(self):
        '''returns a friend list of a profile'''
        friends1 = Friend.objects.filter(profile1=self)
        friends2 = Friend.objects.filter(profile2=self)
        return friends1 | friends2
    
    def add_friend(self, other):
        '''Creates a friendsip between 2 profiles'''
        if not (self == other):
            if not Friend.objects.filter(profile1=self, profile2=other).exists():
                friend = Friend(profile1=self, profile2=other)
                friend.save()
    
    def get_friend_suggestions(self):
        '''Return a list of friend suggestions.'''
        friends = self.get_friends()
        friend_pks = [f.profile1.pk if f.profile1 != self else f.profile2.pk for f in friends]
        suggestions = Profile.objects.all().exclude(pk=self.pk).exclude(pk__in=friend_pks)
        print(suggestions)
        return suggestions
    
    def get_news_feed(self):
        '''Return a list (or QuerySet) of all StatusMessages for the profile and all friends of the profile.'''
        friends = self.get_friends()
        friend_pks = [f.profile1.pk if f.profile1 != self else f.profile2.pk for f in friends]
        news_feed = StatusMessage.objects.filter(profile__in=friend_pks) | StatusMessage.objects.filter(profile=self)
        return news_feed

class StatusMessage(models.Model):
    '''Encapsulates data for a status message'''
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
    '''Encapsulates data for a image'''
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now = True)
    status_message = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)

class Friend(models.Model):
    '''Encapsulates data for a friendship'''
    profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1")
    profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2")
    timestamp = models.DateTimeField(auto_now = True)

    def __str__(self):
        '''Return a string representation of this Friendship'''
        return f"{self.profile1} & {self.profile2}"
    