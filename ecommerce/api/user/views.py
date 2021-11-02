from django.shortcuts import render

import random
# Create your views here.

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