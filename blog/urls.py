from django.urls import path
from django.conf import settings 
from . import views

urlpatterns = [
    path(r'', views.RandomArticleView.as_view(), name="random"),
    path(r'show_all_blog', views.ShowAllView.as_view(), name="show_all_blog"),
    path(r'article/<int:pk>', views.ArticleView.as_view(), name="article"),
]