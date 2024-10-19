from django.urls import path
from django.conf import settings 
from . import views

urlpatterns = [
    path(r'', views.RandomArticleView.as_view(), name="random"),
    path(r'show_all_blogs', views.ShowAllView.as_view(), name="show_all_blogs"),
    path(r'article/<int:pk>', views.ArticleView.as_view(), name="article"),
    # path(r'create_comment', views.CreateCommentView.as_view(), name="create_comment"),
    path(r'article/<int:pk>/create_comment', views.CreateCommentView.as_view(), name="create_comment"),
    path(r'create_article', views.CreateArticleView.as_view(), name="create_article"),
]