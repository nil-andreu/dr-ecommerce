## Ecommerce with React & Django

In this repository, I will be building a full-stack ecommerce with React.js for the frontend, and Django for the backend.

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
