# FOR REGEX
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt # As we will want to make a change by ourselves of the content, so we do not apply intentionally CSRF token
from django.contrib.auth import login, logout # For default login and logout
import re # To run the Regular Expression

# FOR TOKEN
import random
# Define the method for generating token
def generate_session_token(length=20):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))
    '''
    We are going to choose randomly between: [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    for the length we defined (as it is not inclusive the 20)
    For a real app we could put more on mayus and minuscula. We could do the following:
    list1 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, k, r, s, t, u, v, w, x, y, z]
    list2 = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y]
    list3 = [1,2,3,4,5,6,7,8,9]
    list4 = [/,(,),*,-,',!,\,^]
    random.SystemRandom().choice(list1+list2+list3+list4) for _ in range(15)
    
    '''

# Some body is going to make a request to the signin
@csrf_exempt
def signin(request):
    # We identify whether it is a post or get
    if not request.method is "POST":
        return JsonResponse({'error':'Send a post request with valid parameter only'})

    # We will grap the information of the post method made to sign up
    username = request.POST["email"] 
    password = request.POST["password"]

    # VALIDATION PART
    # We do some of the sanitasation, with re.match() to match the pattern of the regular expression and return True if matches
    if not re.match("/[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g", username):
        return JsonResponse({'error':'Enter a valid email'})
    
    # We could also check for the password (uppercase, lowercase, ...)
    if not len(password) > 3 :
        return JsonResponse({"error":"Enter a password of at least 3 characters"})
    
    # ONCE VALIDATION IS PASSED, NOW IS SECURE TO USE USERNAME AND PASSWORD
    UserModel = get_user_model() # I am grabbing a user model
    # Now i will try to grab the user from the database and match its password
    # As we are making a request from another origin, we must apply csrf_exempt --> applied just before this view
    try:
        # 1. Grap the user, obtained with the email field to be equal to username
        user = UserModel.objects.get(email=username)

        # 2. We need to now check the password
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first
            # Where the filter for the one that matches the username, we obtain the values of it and obtain the first
            usr_dict.pop('password')

            # We want to see if in this user we got our session token or not. If already there, meaning the 
            # user is already logged in, we will need ot work on that
            if user.session_token != "0":
                user.session_token = "0" # For the next time when the user logs in, at least then he gets a 0.
                # This way the user will only get once the error that the session is made
                user.save
                return JsonResponse({"error":"Previous session exists"})
            
            # Now is the part that we generate the token
            token = generate_session_token()
            user.session_token = token # Assing the field of the table session_token to the token we just generated
            user.save # We save the token into the user table

            # And finally do the default Django login
            login(request, user) # We login the user

            # If we do now throw this token back, then it is not going to be working
            # We will also pass the information fields of the user that has logged in (we already popped off the password field, so it is secure to pass this way)
            return JsonResponse({"token":token,"user":usr_dict}) 

        else:
            return JsonResponse({"error":"Invalid password"})

    except UserModel.DoesNotExist: # In the case it does not exist
        return JsonResponse({"error":"Invalid email"})




