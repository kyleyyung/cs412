#define data models (objects) for use in the blog application
from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapsulates the data for an Article by some author'''

    #data attributes
    title = models.TextField(blank = False)
    author = models.TextField(blank = False)
    text = models.TextField(blank = False)
    published = models.DateTimeField(auto_now = True)
    image_url = models.URLField(blank = True)

    def __str__(self):
        '''Return a string representation of this Article'''
        return f"{self.title} by {self.author}"

