from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.parsers import JSONParser
from .serializers import Catalog_request
import io
from rest_framework.decorators import api_view


def catalog_addproduct(request):                # Arne Julius
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = Catalog_request(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])                      # Arne Julius
def catalog_display(request):   
    products= Product.product_manager.all()         # Alle Produkte sollen ausgegeben werden
    serializer = Product_serializer(data=products)
    return Response(serializer.data)
