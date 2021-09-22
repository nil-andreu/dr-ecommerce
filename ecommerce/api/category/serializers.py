from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    # We define which is the model that we want to convert to JSON, as well as which fields we want to convert
    class Meta:
        model = Category
        field = ('name, description')

# We do not have to declare any type of new fields, as we are serializing the ones that the model already have.