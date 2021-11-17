from rest_framework import serializers
from .models import *

class Catalog_request(serializers.Serializer):              ##### Arne Julius
    class Meta:
        model = ProductQuerySet
        fields = '__all__'

class Product_serializer(serializers.Serializer):
    class Meta:
        model = product
        fields = '__all__'                                  ##### Arne Julius