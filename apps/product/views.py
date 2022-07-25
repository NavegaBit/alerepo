from rest_framework import viewsets

from .serializer import ProductSerializer, ProductTypeSerializer
from .models import Product, ProductType


# Create your views here.
class ProductView(viewsets.ModelViewSet):
    """
            A viewset for CRUD products.
            """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Create your views here.
class ProductTypeView(viewsets.ModelViewSet):
    """
            A viewset for CRUD products.
            """
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()