from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    # We are using standard urls given by Django: api/login, api/logout, ...
    # But there are some that we want to customize
    path('login/', views.signin, name="signin"),

    # For signing out we also have to capture the id of the user, and we would pass it in the url
    path('logout/<int:id>/', views.signout, name="signout"),
    path('', include(router.urls)),

]