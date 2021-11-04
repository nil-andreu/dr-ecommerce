## Ecommerce with React & Django

In this repository, I will be building a full-stack ecommerce with React.js for the frontend, and Django for the backend. It will include payment gateway with Braintree.

We assume that we have a client, and it has the following goal: "I want to sell t-shirts online".
And we also know that it wants a separate login for admin and for the customer (where the admin will be the one of default panel of Django, and we will build one for the customer).

We could use Coggle to imagine which will be the parts that will have our app. We can think also about the details:

- How will be the models (tables withs its foreign keys) for the products, users, for the orders, ...
- Views
- Urls

## 1. Virtual Environment

First we will create a virtual environment to handle the different dependencies:python -m venv dependencies. Which will create a folder of dependencies.

We will use pipenv to handle the dependencies.
Once it is installed, we will do: pipenv shell. This will generate us a Pipfile, which will have inside all of the dependencies.
And now for installing django, we will use the pipenv: pipenv install django==3.2. (where 3.2. is the version we will use).
This way we will handle easily the installations and dependencies with pip.

Another way we could handle the dependencies is with a requirements.txt, where we could put: pip freeze > requirements.txt

## 2. Django project

We will start the project for Django: django-admin startproject ecommerce.

We will also install the cors headers, which stands for Cross-Origin Resource Sharing. Which is needed when sending multiple requests from multiple resources. As some of the requests will be sended from postman and others from react.
This is very common things to have in all full stack projects.
Check the following documentation for the configuration: https://github.com/adamchainz/django-cors-headers.
What we need to configure in settings:

- APPS_INSTALLED
- MIDDLEWAREs
- CORS_ALLOW_ALL_ORIGINS: to true

Some of them will change in production

We will also in the settings set which are the allowed hosts, which for the moment is '\*' (all). In production i would only want that the React app to interact with it. This would work for public apis.

## 3. Install Django Rest Framework

We will install: pipenv install djangorestframework
And then we put it inside of the INSTALLED_APPS:

- rest_framework
- rest_framework.authtoken; used for custom signup to be created.

As well as we have to put the REST_FRAMEWORK configuration. It will create a default permission class. For authentication we will configure:

- Basic Auth
- Session Auth
- Token Auth: the token based authentification is needed for doing custom auth

## 4. Define URLs

We will define the following URL: path('api-auth', include('rest_framework.urls'))

## 5. How to manage static files

SQLite is not very good for storing images, but it can manage huge amounts of queries.
So what we will do is create a folder, and inside of this folder we will have all of the images.

So we will do the following:

- Create a folder inside of the project directory called media.
- Where inside of it we will create a new folder called images.
- Go to settings.py to configure the media. We will put the following: MEDIA_URL = '/media'
- We will also define a relative path to this media folder: MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
- It needs to be mentioned in the URL as well. So for this we will go to the urls.py and do the following:
  - from django.conf.urls.static import static
  - from django.conf import settings
  - And then define another urlpattern:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    And from settings we can reference to MEDIA_URL we just created. As well as we define the parameter of the document root in order to be able to store things there.

So this way is how we handle the media resource

## 6. Setting API structure

Now we will create the app which will handle all the requests of the api.
Inside of this app for the api, we will create further smaller apps:

- Category
- Order
- Payment
- Product
- User

This is, i will create an in the project folder which will be the api. And inside the different folders for the actual Django apps.
This way we can ensure the scalability of the project and if we had different teams each one could focus on an app.

So what we will do is: django-admin startapp api. Inside of the project directory.

And then inside of the folder api, we want to create the before mention mini-apps.

We must also go to the settings, and register the api app as well as the mini-apps.

## 7. Configure root api

So this api app is going to be the root for all the apis. As this app is inside of the settings of our project, it means that we can use it for the urls.py: path('api/', include('api.urls')). Which means that we are creating a new path to handle all the requests in the api urls.py file (which we need to create).

Inside of the urls.py of our api app, we will import the authtoken for views, which we will use in the future.

We will then create the array of urlpatterns. Where we will have the root/home route for the APIs. So it would be: localhost:8000/api/.

For creating the home, we have to create it in the views. So we need to go inside of the views.py and create the home view function.
We put the following: from django.http import JsonResponse
And then define the view;

    def home(request):
        return JsonResponse({'info': 'Django course')

Where we import the JsonResponse, and then we will return in the home (localhost:8000/api/) the json which will be the key-value pair.

## 8. Setting up category model and admin

We will now work on the category. Which will have the following:

<ol type="a">
  <li>Create a model</li>
  <li>Register in admin</li>
  <li>Serializers.py file to serialize data in JSON</li>
  <li>Views to get all category</li>
  <li>Setup url</li>
</ol>

All of this has to be inside of the category file. So we need to create:

- urls.py
- serializers.py

And then we will create the model in models.py as well as register it in the admin.py. For this to work has to be inside of the INSTALLED_APPS, so we add the 'api.category', as it is inside of the folder of api and the category is the name of the app (as we can see if we go to the apps.py).

Check that now for the version of Django of >=3.2., we need to edit the apps.py to put the name as 'api.category'. As if in INSTALLED APPS we put this and in the name is only 'category' it will give us an error.

## 9. Serialize data in Django

Django is about easying the syntax, and not focus on the back of the things. It is all about an abstraction.

So we will need to do now the serializations.
For this, we are going to create the serializator. We go to the serializers.py file, and we import: from rest_framework import serializers, as well as the model we defined.

And we create the following class, which will be the serializer:

```{python}
  class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # We define which is the model that we want to convert to JSON, as well as which fields we want to convert
    class Meta:
        model = Category
        fields = ('name', 'description')

```
We are using the HyperlinkedModelSerializer because if we use the normal Serializer, we will not be able to obtain the data when making get requests.

## 10. Setting up views and url

We want to work now with the viewsets and the router.

First we will do the importations:

```{python}
  from rest_framework import viewsets
  from .serializers import CategorySerializer
  from .models import Category
```

Where the viewsets will be used to create the api view.

Then we define the CategoryViewSet. The viewset that we are going to define is by using the model Category, for this we use the viewsets.ModelViewset.

```{python}
  class CategoryViewSet(viewsets.ModelViewSet):
    # We have to mention two things:
    # 1. Which is the query, the data that we bring from the database
    # 2. Based on the serializer we have wrote, convert this data into JSON

    # 1. Build the query
    queryset = Category.objects.all().order_by('name')

    # 2. Define the class responsible for serializing the data
    serializer_class = CategorySerializer
```

And now we want to set the url. For this, remember that in the urls.py of the project, we defined a path named 'api/', which includes the api.urls.
Then in the api.urls, we defined: path('', home, name="api_home").
But now we need to define another path in this url of the api: path('category/', include('api.category.urls')). So this will search for the urls in the path of api/category/ inside of the urls of the app category.

This url of the category is going to be handler by the django rest framework router: from rest_framework import router.
And the code that we are putting then is the following:

```{python}
  from rest_framework import routers
  from django.urls import path, include # We will also need to import the django urls

  from . import views # We need to import all the views, so we are importing the full file

  router = routers.DefaultRouter()

  router.register(r'', views.CategoryViewSet)

  urlpatterns = [
    path('', include(router.urls))
  ]
```

So in the urls, we follow this process:

- Create the router with a type (in our case DefualtRouter)
- Register this router in a path with a Viewset
- And then add this router to the urlpatterns (we do this because we are using the DefualtRoute)

And for creating the whole api, we follow this process:

<ol type="a">
  <li>Create a model in <bold>models.py</bold></li>
  <li>Register in admin in <bold>admin.py</bold></li>
  <li><bold>Serializers.py</bold> file to serialize data in JSON</li>
  <li>Views to get all category inside of <bold>views.py</bold></li>
  <li>Setup url inside of the <bold>urls.py</bold></li>
</ol>

Now if we look to the localhost:8000/api/category/, we will see what the Django Rest Framework provides for default for our API a template for making the queries.

We could test this api by creating some example Categories. And then making the query with Postman to the url before mentioned. 
Also if for the moment we call to /api/, we will see what we stated a JsonResponse:
```{javascript}
  {
    "info": "Django course"
  }
```

## 11. Making the same process for products

Now we are going to same process as before for the products.

In the model of product, we want the following fields:
- Name
- Description
- Price
- Stock
- is_active
- image
- category: which is going to be a foreign key to Category, for this we need to import from api.category.models.
- created_at

Once that the model is created, we are going to register it in the admin.

```{python}
  from django.db import models
  from api.category.models import Category

  # Create your models here.
  class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField()

    # For image, we have to set upload_to, where is the path that will search for the images. 
    image = models.ImageField(upload_to='images/') 

    # This way we can relate tables in different apps
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # On delete, we do not want to delete all the category
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
```
When making this migration, we will need to install Pillow. Which is a python package needed for handling the images.

Then we have to create the serializer. Once created, we create the view.
But note that for the case that we are handling an image, we need to make some changes. As we want to make sure that this serializer will give us the full url, so we will be able then to access it. For handling this, we will need to create a new field inside the serializer. Which is the one that will be handling the image.
```{python}
  from rest_framework import serializers
  from .models import Product

  class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # We need to crete the field of Image, as for images we need to make an specialized field of Rest Framework
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, required=False)
    # We are putting the following params:
    # - max_length: None. There is not a max length, otherwise our url could not be complete
    # - allow_empty_file: False
    # - allow_null:True.
    # - required: False.
    # Those parameters are the required ones, we can check in the documentation

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category')
        # We also do not want all the fields, as for example the created_add is only for administration of the ecommerce
```
Note that we are not using the '__all__' in the fields, to indicate we want all of them. As we are creating a new field which is the image field.

And for creating the viewset:
```{python}
  from django.shortcuts import render
  from rest_framework import viewsets
  from .models import Product
  from .serializers import ProductSerializer

  # Create your views here.
  class ProductViewset(viewsets.ModelViewSet):
    # Remember that we need to define the query
    queryset = Product.objects.all().order_by('-price')
    serializer_class = ProductSerializer
```

And finally we create the urls:
```{python}
  from django.urls import path, include
  from rest_framework import routers

  from . import views

  router = routers.DefaultRouter()
  router.register(r'', views.ProductViewset)

  urlpatterns = [
    path('', include(router.urls))
]
```

## 12. Setting up Custom user in model

We will use the Django user auth handling.

Now what will happen also is that the serialization will be tricky, as there is data that will also be sent to the server (not only receiving as far it has happened).

First of all, we will create the model of the User inheriting the User model already created by the Django. We will inherit the default, as in the future we might want to sign up with other fields:
- Email
- Age
- Year of birth
- ...
As django by default log in is with username and password.

The code for doing this is the following:
```{python}
  from django.contrib.auth.models import AbstractUser

  class User(AbstractUser):
    pass
```

We will create this inside of the user mini-app.
And put inside of the models.py the following code:
```{python}
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
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

    # We will need to work on the session based token, so we will create this
    session_token = models.CharField(max_length=10, default=0)
```

Then we have to update this model in the admin panel.

What happens now is that we can't follow the basic flow of:
- create model
- register in admin
- serializers.py
- views
- and then setup urls.py

This changes drastically when you are dependent on some existing models and there is a reason for that: in Django admin the models of Groups and Users are already given to me. So if i somehow depend on them, and my app is not finished yet, i am going to have a conflict.
So if the model is totally new, it does not depend on any abstract user, any additional functionality is provided by Django, then the before flow is great.
But the good flow we need to follow now is:
<ol type="a">
  <li>Create a model based on an existing model<bold>Abstract User</bold></li>
  <li>Serialize, vies and urls </li>
  <li><bold>Register</bold> app in the admin</li>
  <li><bold>Debug it</bold></li>
</ol>
This is the flow that the majority of companies like to follow, as half baked applications of the Django, if you plug it into the admin, they are going to potentially result in the error.

WE COULD DO THE FOLLOWING:
For solving these errors of dependency, i need to go to settings.py, and add the following line of code to set how we will handle the users:
```{python}
  AUTH_USER_MODEL = "user.CustomUser"
```
As we are actually writing custom user model.
And we are saying that from the user app, use CustomUser.
Once i have done this, i can makemigrations and migrate. And then run the server again.

BUT INSTEAD WE WILL FINISH THE USER APP AND THEN WILL DO THE ADMIN REGISTRATION AND ADDING IN INSTALLED_APPS
How now we are going to serialize it.
Remember, that in python i can use ** operator, which allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call. This operator is used when we have a list of multiple arguments taken up in a function, and by using these operator.

Since data is coming up in json format, we will need to deal with that for registering for example users. We can access the data of a serializer with serializer.validated_data --> from this validated data that is in a dictionary i can pop off each of the keys with the ** operator: **validated_data.
So in the serializer, we might want to create two methods:
- .create():
- .update(): 

Example of ** operator:
```{python}
  class Man:
    name = "John"
  
  # Create a new object
  one = Man()
  print(one.name) # And would print John

  # We can set an attribute with the following
  setattr(one, 'name', 'Nil')
  '''Where setattr takes the following parameters:
  - the variable we want to change
  - the property i want to change
  - the new value i want for that property
  '''
```

So now we are going to create the serializers.py and urls.py. And go to the serializers.py.

Then we go to the views, where we are going to sign in the user, sign out, generate the token, ...
For the generation of the token:
```{python}
  # chr(97) will be giving me a, if chr(98) is giving me b
  # This method creates letters based on numbers
  import random

  # Random has a method of SystemRandom, and this has a method which pass a list --> and will choose randomly a value from the lsit
  # random.SystemRandom().choice(['a','b','c'])
  random.SystemRandom().choice([chr(i) for i in range(97, 123)])
  # So i defined a loop for range 97 to 123 (the last one is not inclusive) and choose between those numbers
```
Knowing this, we will create in views a method for the string generation.

For the sign up of the user, we need to do some validation. For this, we can go to the web of regexr.com.
One validator we can use is: /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g
We will go to views.py and check


#### Auth

For making the authentification with Facebook, Google, ... We need to install the pacjage: https://github.com/RealmTeam/django-rest-framework-social-oauth2. We can see the documentation in this repository README file.

Yoou can also look for the tutorial: https://www.youtube.com/watch?v=wlcCvzOLL8w&list=RDCMUC1mxuk7tuQT2D0qTMgKji3w&start_radio=1.