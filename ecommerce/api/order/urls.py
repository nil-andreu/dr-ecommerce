from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewset)

urlpatterns = [
    path('add/<str:id>/<str:token>/', views.add_order, name="order_add"),
    path("", include(router.urls))
]
