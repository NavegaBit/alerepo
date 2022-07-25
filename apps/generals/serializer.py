from rest_framework import serializers
from .models import CompanyData, Promotion, SocialNet


class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialNet
        fields = ['name', 'share', 'ico', 'image', 'active', 'created_at', 'updated_at']


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ['name', 'description', 'image', 'image', 'active', 'created_at']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyData
        fields = ['name', 'email', 'image', 'ico', 'favico', 'key', 'visual', 'active', 'created_at', 'updated_at']
