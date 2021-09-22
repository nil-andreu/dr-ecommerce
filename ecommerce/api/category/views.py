from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category

# Extending the viewset with the model viewset, to create a viewset based on a model
class CategoryViewSet(viewsets.ModelViewSet):
    # We have to mention two things:
    # 1. Which is the query, the data that we bring from the database
    # 2. Based on the serializer we have wrote, convert this data into JSON

    # 1. Build the query
    queryset = Category.objects.all().order_by('name')

    # 2. Define the class responsible for serializing the data
    serializer_class = CategorySerializer
