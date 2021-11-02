from django.shortcuts import render

import random
# Create your views here.

# Define the method for generating token
def generate_session_token(length=20):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))