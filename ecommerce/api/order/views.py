from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.contrib.auth import get_user_model

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

# Create your views here.
class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer