from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt # to make it excempt the react calls

import braintree

# the configuration we have in the sandbox account
gateway = braintree.BraintreeGateway(
  braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='zjwjjcy88hw4z9v2',
    public_key='hzbxz9mggqrn8rjn',
    private_key='e5dad8bc3af5d7b3435c1629807d328c'
  )
)

# Checking if user is signed up
def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.all(pk=id)
        if user.session_token == token: #if the session token stored in the database is the same as the token that the user is carrying 
            return True
        return False
    except UserModel.DoesNotExist:
        return False
    
@csrf_exempt
def generate_token(request, id, token):