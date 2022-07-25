from rest_framework import routers
from .views import CompanyViewSet, PromotionViewSet, SocialViewSet

company_patterns = routers.DefaultRouter()
company_patterns.register(r'company', CompanyViewSet, basename='Company')
company_patterns.register(r'promotion', PromotionViewSet, basename='Promotion')
company_patterns.register(r'social', SocialViewSet, basename='Social')

