from django.db import models
from api.category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    is_active = models.BooleanField(default=True)

    # For image, we have to set upload_to, where is the path that will search for the images. 
    image = models.ImageField(upload_to='images/', blank=True, null=False) 

    # This way we can relate tables in different apps
    category = models.ForeignKey(Category, on_delete=models.SET_NULL) # On delete, we do not want to delete all the category
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
