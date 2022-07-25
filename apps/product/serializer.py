from .models import ProductType, Product
from rest_framework import serializers


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['name', 'active']
        read_only_fields = ['created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'product_type', 'image', 'active', 'description', 'meta_text']
        read_only_fields = ['created_at', 'updated_at']
