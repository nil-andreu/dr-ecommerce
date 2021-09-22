from rest_framework import routers
from django.urls import path, include # We will also need to import the django urls

from . import views # We need to import all the views, so we are importing the full file

# We will use the default router
router = routers.DefaultRouter()

# And now we register the before route in a path. This path is going to be the empty one
router.register(r'', views.CategoryViewSet)
# So the full path is being: 'api/category/'.

# And now we add this route to the urlpatterns
urlpatterns = [
    path('', include(router.urls))
]
# We do this step because we are using the DefaultRouter type

