from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name="api_home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('users/', include('api.user.urls'))

]