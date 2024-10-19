#blog/views.py
# views to show the blog app

from typing import Any
from django.shortcuts import render
from django.urls import reverse
from . models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
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

class CreateCommentView(CreateView):
    '''a view to show/process the create comment form
    on GET: send back the form
    on POST: read the for,m data, create an isntant of Comment; save to database;'''
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    #what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        #return "/blog/show_all"
        # return reverse("show_all")
        return reverse("article", kwargs=self.kwargs)
    
    def form_valid(self, form):
        '''this method executes after form submission'''

        #find the article with the PK from the URL
        article = Article.objects.get(pk=self.kwargs['pk'])

        # attach the article to the comment
        # (form.instance is the new comment object)
        form.instance.article = article

        # deleguate work to the superclass version of this method
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''buld the template context data -- a dict of key-value pairs'''
        context = super().get_context_data(**kwargs)

        article = Article.objects.get(pk=self.kwargs['pk'])

        context['article'] = article

        return context
    
class CreateArticleView(CreateView):
    '''A view to create a new Article and save it to the database.'''
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"


