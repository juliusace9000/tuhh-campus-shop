from rest_framework import serializers
from .models import #Catalogrequest oder so

class Catalog_request(serializers.Serializer):
    class Meta:
        model = #catalogrequest
        fields = '__all__'