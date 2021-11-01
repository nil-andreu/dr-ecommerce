from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # We need to crete the field of Image, as for images we need to make an specialized field of Rest Framework
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, required=False)
    # We are putting the following params:
    # - max_length: None. There is not a max length, otherwise our url could not be complete
    # - allow_empty_file: False
    # - allow_null:True.
    # - required: False.
    # Those parameters are the required ones, we can check in the documentation

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')
        # We also do not want all the fields, as for example the created_add is only for administration of the ecommerce