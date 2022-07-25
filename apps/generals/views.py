from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.response import Response

from .serializer import CompanySerializer, PromotionSerializer, SocialSerializer
from .models import CompanyData, Promotion, SocialNet


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Api for Company data
    """
    queryset = CompanyData.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class PromotionViewSet(viewsets.ModelViewSet):
    """
    Api for Promotions
    """
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class SocialViewSet(viewsets.ModelViewSet):
    """
    Api for Social
    """
    queryset = SocialNet.objects.all()
    serializer_class = SocialSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
