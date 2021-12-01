from django.db import models

'''We need to import the dependencies for making the orders
These orders are going to be made by the User.
We will also do orders for the products
'''
from api.user.models import CustomUser
from api.product.models import Product

# Create your models here.
class Order(models.Model):
    # We are going to bring the user
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    product_names = models.CharField(max_length=500)
    total_products = models.CharField(max_length=500, default=0)
    total_amount = models.CharField(max_length=50, default=0)


    # We might want a transaction id that will be needed later for validating transactions
    transaction_id = models.CharField(max_length=200, default=0)


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


