from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous') # If there is no name, the default will be "Anonymous"
    # In the case of the email, i want this to be unique
    email = models.EmailField(max_length=200, unique=True)
    username = None # This username field is already by default in the model
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # I am not signing up the user based on the username, but rather
    # i will be modifying this username field
    USERNAME_FIELD = 'email' # This username field will now be validated with the email

    # And also have some fields that have to be required, in our case is none
    REQUIRED_FIELDS = []

    # We will need to work on the session token based, so we will create this
    session_token = models.CharField(max_length=20, default=0)