from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Category

class ProductListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(is_active=True, quantity__gt=0)
        data = [{'name': product.name, 'price': product.price, 'description': product.description,
                 'quantity': product.quantity, 'category': product.category.name} for product in products]
        return Response(data, status=status.HTTP_200_OK)
