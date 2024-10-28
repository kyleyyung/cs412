from django.urls import path
from django.conf import settings 
from . import views

urlpatterns = [
    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name="show_profile"),
    path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile"),
    path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name="create_status"),
    path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name="update_profile"),
    path(r'status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name="delete_status"), #new delete status path
    path(r'status/<int:pk>/update', views.UpdateStatusMessageView.as_view(), name="update_status"), #new update status path
    path(r'profile/<int:pk>/add_friend/<int:other_pk>', views.CreateFriendView.as_view(), name="create_friend"), # new add friend path
    path(r'profile/<int:pk>/friend_suggestions', views.ShowFriendSuggestionsView.as_view(), name="show_suggestions"), # new friend suggestion path
    path(r'profile/<int:pk>/news_feed', views.ShowNewsFeedView.as_view(), name="show_news_feed"), # new news feed path
]