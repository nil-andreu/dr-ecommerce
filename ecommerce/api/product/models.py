from django.db import models
from api.category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True,blank=True)

    # For image, we have to set upload_to, where is the path that will search for the images. 
    image = models.ImageField(upload_to='images/', blank=True, null=True) 

    # This way we can relate tables in different apps
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # On delete, we do not want to delete all the category
    # Note that if the category will be set to null when deleted, it is a requisite to put null=True in this model
    # As by default it is False, so there will be an error.

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
