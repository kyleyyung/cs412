from django.urls import path
from django.conf import settings 
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.ShowAllView.as_view(), name="home"), # home page
    path('results', views.ShowAllView.as_view(), name='results'), # display result of search query page
    path(r'product/<int:pk>', views.ShowProductPageView.as_view(), name="show_product"), # display product page
    path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name="show_profile"), # display profile page
    path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile"), # create profile page
    path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name="update_profile"), # update profile page
    path(r'create_product', views.CreateProductView.as_view(), name="create_product"), # create product page
    path(r'product/<int:pk>/update', views.UpdateProductView.as_view(), name="update_product"), # update product page
    path(r'product/<int:pk>/delete', views.DeleteProductView.as_view(), name="delete_product"), # delete product page
    path(r'product/<int:pk>/create_review', views.CreateReviewView.as_view(), name="create_review"), # create review page
    path(r'product/<int:pk>/add_order', views.AddOrderView.as_view(), name="add_order"), # add product to order page
    path(r'review/<int:pk>/delete', views.DeleteReviewView.as_view(), name="delete_review"), # delete review page
    path(r'review/<int:pk>/update', views.UpdateReviewView.as_view(), name="update_review"), # update review page
    path(r'order/<int:pk>', views.ShowOrderPageView.as_view(), name="show_order"), # display order page
    path(r'order/<int:pk>/update', views.UpdateOrderItemView.as_view(), name="update_orderitem"), # update order page
    path(r'order/<int:pk>/delete', views.DeleteOrderItemView.as_view(), name="delete_orderitem"), # order item delete page
    path(r'order/<int:pk>/confirm', views.ConfirmOrderView.as_view(), name="confirm"), # order confirmation page
    # authentication views
    path('login/', auth_views.LoginView.as_view(template_name='project/login.html'), name='login'), # login page
    path('logout/', auth_views.LogoutView.as_view(template_name='project/logout.html'), name='logout'), # logout page
]