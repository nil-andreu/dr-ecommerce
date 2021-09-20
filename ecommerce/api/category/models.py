from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, empty=False)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True) # Automatizally takes the now date time when the category is added
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name