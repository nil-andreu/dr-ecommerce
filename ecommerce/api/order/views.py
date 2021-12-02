import json
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# We are going to validate the user session and will grap the user id and its token
def validate_user_session(id, token):
    # So whoever requests this url, we expect it to bring id and the token

    # We are going to get the user model
    UserModel = get_user_model()

    # And now we will try to effectively obtain it or return false
    try:
        user = UserModel.objects.get(pk=id)

        # We are going to check that the user is authenticated by its token
        if user.session_token == token:
            return True
        else:
            # Meaning that this token is not the session token of that user
            return False

    except UserModel.DoesNotExist:
        return False

# It is important to use the csrf_excempt
@csrf_exempt
def add_order(request, id, token):
    
    # We are checking if the user is validated
    if not validate_user_session(id, token):
        # Meaning the user is not validated we send a missage and a code for that error
        return JsonResponse({"error":"User is not authenticated", "code":"500"})
    
    if request.method == "POST":
        # If it is post, then we need to collect some variables from it
        user_id = id # This id will come directly

        # And now the variables that come from the front end
        transaction_id = request.POST["transaction_id"]
        amount = request.POST["amount"]
        products = request.POST["products"]

        # Now we need to compute how many products are
        total_products = len(products.split(",")[:-1]) # As products is a list and we split by , and -1 is to create a new array of x * 1.

        # We need to grap the user model as well
        UserModel = get_user_model()
        try:
            # If the user exists, then we will pass all the before information to that user
            user = UserModel.objects.get(pk=user_id)

            # We construct first this Order
            order = Order(user=user, product_names=products, total_products=total_products, transaction_id=transaction_id, total_amount=amount)
            order.save() # And for that user, we save the order it placed
            return JsonResponse({"success":True, "error":False}) # We would return that for doing a check


        except UserModel.DoesNotExist:
            return JsonResponse({"error":"User does not exist"})