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
