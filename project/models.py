# Kyle Yung, yungk@bu.edu
# Creates the models used in the Application

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    '''Encapsulates the data for a Profile'''

    # data attributes
    first_name= models.TextField(blank = False)
    last_name = models.TextField(blank = False)
    email = models.TextField(blank = False)
    image_url = models.URLField(blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        '''Return a string representation of this Profile'''
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse("show_profile", kwargs={'pk': self.pk})
    
    def get_products(self):
        '''Retrieve all status Mmssages for this Profile'''

        # use the ORM to filter products where this instance of seller is the foreign key
        products = Product.objects.filter(seller=self)
        return products
    
    def get_orders(self):
        '''Retrieve all status Mmssages for this Profile'''

        # use the ORM to filter Orders where this instance of Profile is the foreign key
        orders = Order.objects.filter(profile=self)
        return orders

class Product(models.Model):
    '''Encapsulates the data for a Product'''

    # data attributes
    title = models.TextField(blank = False)
    description = models.TextField(blank = False)
    price = models.TextField(blank = False)
    seller = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="products")
    image_url = models.URLField(blank = True)

    def __str__(self):
        '''Return a string representation of this Product'''
        return f"{self.title} for {self.price}"
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse("show_product", kwargs={'pk': self.pk})
    
    def get_reviews(self):
        '''Retrieve all reviews for this Product'''

        # use the ORM to filter reviews where this instance of Product is the foreign key. Order by time sent.
        reviews = Review.objects.filter(product=self).order_by('-timestamp')
        return reviews
    
class Review(models.Model):
    '''Encapsulates the data for a Review'''

    # data attributes
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.TextField(blank = False)
    timestamp = models.DateTimeField(auto_now = True)
    image_file = models.ImageField(blank=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="reviews")

    def get_images(self):
        # use the ORM to filter images where this instance of review is the foreign key
        images = Image.objects.filter(review=self)
        return images

    def __str__(self):
        '''Return a string representation of this relationship'''
        return f"{self.profile} for {self.product}"
    
class Order(models.Model):
    '''Encapsulates data for a items in Profile's orders'''

    # define 3 possible status for orders.
    status_choices = [("cart", "Cart"), ("shipping", "Shipping"), ("complete", "Complete"),]
    
    # data attributes
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="order")
    timestamp = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        '''Return a string representation of this relationship'''
        return f"{self.profile} ordered at {self.timestamp}, {self.status}"
    
    def get_absolute_url(self) -> str:
        '''return the URL to redirect to after successful create'''
        return reverse("show_order", kwargs={'pk': self.pk})
    
class OrderItem(models.Model):
    '''Encapsulates data for an item in a Profile's orders'''
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        '''Return a string representation of this relationship'''
        return f"{self.order.profile} ordered {self.quantity} of {self.product.title}"
    
class Image(models.Model):
    '''Encapsulates data for a image'''
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now = True)
    review = models.ForeignKey("Review", on_delete=models.CASCADE)