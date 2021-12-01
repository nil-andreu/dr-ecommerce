from django.db import models

'''We need to import the dependencies for making the orders
These orders are going to be made by the User.
We will also do orders for the products
'''
from api.user.models import CustomUser
from api.product.models import Product

# Create your models here.
class Order(models.Model):
