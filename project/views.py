#project/views.py
# views to show the mini amazon app

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from typing import Any
from django.shortcuts import get_object_or_404
from django.contrib.auth import login   
from decimal import Decimal, InvalidOperation

# Create your views here.

class ShowAllView(ListView):
    '''A view to show all Products (home page)'''

    model = Product
    template_name = 'project/home.html'
    context_object_name = 'products'
    paginate_by = 50

    def get_queryset(self):
        '''return the set of Results'''

        #use the superclass version of query set
        qs = super().get_queryset()

        # if we have a search parameter, use it to filter the query set
        if 'title' in self.request.GET:
            title = self.request.GET['title']
            if title: # not empty string
                qs = Product.objects.filter(title__icontains = title)
        return qs
    
class ShowProductPageView(DetailView):
    '''A view to show a product'''

    model = Product
    template_name = 'project/show_product.html'
    context_object_name = 'product'
    form_class = AddOrderForm

    def get_context_data(self, **kwargs):
        '''provides context data to the template.'''

        context = super().get_context_data(**kwargs)
        # Add the form to the context
        context['form'] = AddOrderForm()
        return context
    
    def form_valid(self, form):
        """Handles valid form submissions."""
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        # Get the logged-in user's profile
        profile = get_object_or_404(Profile, user=self.request.user)

        # Get or create the user's cart (Order with status="cart")
        cart_order, created = Order.objects.get_or_create(
            profile=profile,
            status="cart",
        )

        # Get the quantity from the form
        quantity = form.cleaned_data["quantity"]

        # Add the product to the cart
        order_item, item_created = OrderItem.objects.get_or_create(
            order=cart_order,
            product=product,
        )
        if not item_created:
            # Update the quantity if the item already exists
            order_item.quantity += quantity
        else:
            # Set the quantity for the new item
            order_item.quantity = quantity
        order_item.save()

        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    '''A view to show a profile'''

    model = Profile
    template_name = 'project/show_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        """Fetch the Profile based on the pk in the URL."""
        return get_object_or_404(Profile, pk=self.kwargs['pk'])

class CreateProfileView(CreateView):
    '''a view to show/process the create profile form
    on GET: send back the form
    on POST: read the form data, create an instant of profile; save to database;'''
    form_class = CreateProfileForm
    template_name = "project/create_profile_form.html"

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        #return "/mini_fb/show_all"
        # return reverse("show_all")
        return self.object.get_absolute_url()
    
    def get_context_data(self, **kwargs: Any):
        '''provides context data to the template.'''

        context = super().get_context_data(**kwargs)
        # Add the form to the context
        context['form2'] = UserCreationForm(self.request.POST)
        return context
    
    def form_valid(self, form):
        '''this method executes after form submission'''
        form2 = UserCreationForm(self.request.POST)
        # if not valid, let super class handle
        if not form2.is_valid():
            return super().form_invalid(form2)
        # if it is, save it to database
        pv = form2.save()
        # attach instance to profile
        profile = form.instance
        profile.user = pv
        profile.save()
        login(self.request, pv)
        return redirect('show_profile', pk=profile.pk)
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''a view to show/process the update of a profile'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'project/update_profile_form.html'
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class CreateProductView(LoginRequiredMixin, CreateView):
    '''a view to show/process the create product form
    on GET: send back the form
    on POST: read the form data, create an instant of a product; save to database;'''
    form_class = CreateProductForm
    template_name = 'project/create_product_form.html'

    #what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse('show_profile', kwargs={'pk': self.object.seller.pk})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def form_valid(self, form):
        '''this method executes after form submission'''
        profile = Profile.objects.get(user=self.request.user)
        # attach the profile to the product
        form.instance.seller = profile
        return super().form_valid(form)
    
class CreateReviewView(LoginRequiredMixin, CreateView):
    '''a view to show/process the create review form
    on GET: send back the form
    on POST: read the form data, create an instant of a review; save to database;'''
    form_class = CreateReviewForm
    template_name = 'project/create_review_form.html'

    # what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse('show_product', kwargs={'pk': self.object.product.pk})
    
    def form_valid(self, form):
        '''this method executes after form submission'''

        #find the product with the PK from the URL
        product = self.get_object()
        profile = Profile.objects.get(user=self.request.user)
        # attach the review's profile to profile
        # attach the review's product to product
        form.instance.product = product
        form.instance.profile = profile
        # save the review to database
        rv = form.save()

        files = self.request.FILES.getlist('files')

        for file in files:
            img = Image(review = rv, image_file = file)
            img.save()

        # deleguate work to the superclass version of this method
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''build the template context data -- a dict of key-value pairs'''
        context = super().get_context_data(**kwargs)

        product = self.get_object()
        # Add the product to the context
        context['product'] = product

        return context
    
    def get_object(self) -> str:
        return get_object_or_404(Product, pk=self.kwargs['pk'])
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class UpdateProductView(LoginRequiredMixin, UpdateView):
    '''a view to show/process the update product form
    on GET: send back the form
    on POST: read the form data, update the instant of a product; save to database;'''
    model = Product
    form_class = UpdateProductForm
    template_name = 'project/update_product_form.html'

class UpdateReviewView(LoginRequiredMixin, UpdateView):
    '''a view to show/process the update of a review
    on GET: send back the form
    on POST: read the form data, update the instant of a review; save to database;'''
    model = Review
    form_class = UpdateReviewForm
    template_name = 'project/update_review_form.html'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful update'''
        return reverse("show_product", kwargs={'pk': self.object.product.pk})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class DeleteProductView(LoginRequiredMixin, DeleteView):
    '''a view to show/process the deletion of a product'''
    model = Product
    template_name = 'project/delete_product_form.html'
    context_object_name = 'product'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse("show_profile", kwargs={'pk': self.object.seller.pk})
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
class DeleteReviewView(LoginRequiredMixin, DeleteView):
    '''a view to show/process the deletion of a review'''
    model = Review
    template_name = 'project/delete_review_form.html'
    context_object_name = 'review'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse("show_product", kwargs={'pk': self.object.product.pk})
    
class ShowOrderPageView(LoginRequiredMixin, TemplateView):
    '''A view to show a user's orders'''
    model = Order
    template_name = "project/show_order.html"
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        """Build the context data for the order."""
        context = super().get_context_data(**kwargs)

        # Get the logged-in user's profile
        profile = Profile.objects.get(user=self.request.user)

        # Retrieve all cart items from the user's profile
        cart_order = Order.objects.filter(profile=profile, status="cart").first()

        total_price = Decimal("0.00")

        if cart_order is not None:
            for item in cart_order.items.all():
                try:
                    # Cast price to Decimal
                    product_price = Decimal(item.product.price)
                    total_price += product_price * item.quantity
                except InvalidOperation:
                    # Handle invalid price values
                    product_price = Decimal("0.00")  # default to 0.00 for invalid values
                    total_price += product_price * item.quantity
        
        # Add the order to the context
        context["order"] = cart_order
        # Add the items to the context
        context['items'] = cart_order.items.all() if cart_order else [] 
        # Add the total price to the context
        context["total_price"] = total_price
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle the purchase items action."""
        # Get the user's current cart
        profile = Profile.objects.get(user=self.request.user)
        order = get_object_or_404(Order, profile=profile, status="cart")

        # Change status to "complete" and clear cart items
        order.status = "complete"
        order.save()
        order.items.all().delete()

        # Redirect to the confirmation page
        return redirect('confirm', pk=order.pk)
    
class AddOrderView(LoginRequiredMixin, CreateView):
    '''a view to show/process the add to order form
    on GET: send back the form
    on POST: read the form data, update the instant of a order; save to database;'''
    model = OrderItem
    form_class = AddOrderForm
    template_name = 'project/add_order_form.html'

    def get_context_data(self, **kwargs):
        """Add the product to the context for rendering the form."""
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))  # Get the product based on URL parameter
        context['product'] = product
        return context

    def form_valid(self, form):
        '''this method executes after form submission'''
        # Get the product from the URL
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        # Get or create the logged-in user's cart
        profile = get_object_or_404(Profile, user=self.request.user)
        cart_order, created = Order.objects.get_or_create(profile=profile, status="cart")

        form.instance.order = cart_order
        form.instance.product = product

        try:
            existing_order_item = OrderItem.objects.get(order=cart_order, product=product)
            existing_order_item.quantity += form.cleaned_data['quantity']
            existing_order_item.save()
            self.object = existing_order_item  # Set the existing item as the object for success_url
        except OrderItem.DoesNotExist:
            # Save the new OrderItem
            return super().form_valid(form)
        return redirect('show_product', pk=product.pk)

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful update'''
        return reverse("show_order", kwargs={'pk': self.object.order.profile.pk})
    

class UpdateOrderItemView(UpdateView):
    '''a view to show/process the update orderitem form
    on GET: send back the form
    on POST: read the form data, update the instant of a orderitem; save to database;'''
    model = OrderItem
    form_class = UpdateOrderItemForm
    template_name = "project/update_orderitem_form.html"
    context_object_name = "order_item"

    def get_object(self, queryset=None):
        """Retrieve the specific OrderItem to update."""
        # Ensure the logged-in user owns the item
        return get_object_or_404(OrderItem, pk=self.kwargs["pk"],order__profile__user=self.request.user,)

    def form_valid(self, form):
        """Process the form when valid."""
        # Save the updated quantity
        form.save()
        return redirect('show_order', pk=self.object.order.profile.pk)
    
    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse("show_order", kwargs={'pk': self.object.order.profile.pk})

class DeleteOrderItemView(LoginRequiredMixin, DeleteView):
    '''a view to show/process the deletion of a order item'''
    model = OrderItem
    template_name = 'project/delete_orderitem_form.html'
    context_object_name = 'order_item'

    def get_success_url(self) -> str:
        '''return the URL to redirect to after successful delete'''
        return reverse("show_order", kwargs={'pk': self.object.order.profile.pk})
    
class ConfirmOrderView(LoginRequiredMixin, TemplateView):
    '''a view to confirm the order form
    on GET: send back the form
    on POST: read the form data, update the instant of a Order; save to database;'''
    model = Order
    template_name = 'project/confirmation.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        """Build the context data for the confirmed order."""
        context = super().get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=self.kwargs['pk'], profile__user=self.request.user)
        return context
