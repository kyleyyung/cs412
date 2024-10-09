#blog/views.py
# views to show the blog app

from django.shortcuts import render
from . models import *
from django.views.generic import ListView, DetailView
import random
class ShowAllView(ListView):
    '''A view to show all Articles'''

    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

class RandomArticleView(DetailView):
    '''Show one articlw selected at random'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

    def get_object(self):
        '''Return the instance of the Article object to show.'''

        # get all articles
        all_articles = Article.objects.all() # SELECT *
        # pick one at random
        return random.choice(all_articles)

class ArticleView(DetailView):
    '''Show one article by its primary key'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'



