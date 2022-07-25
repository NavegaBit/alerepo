from rest_framework.routers import DefaultRouter

from apps.product.views import ProductView, ProductTypeView


products_urls = DefaultRouter()

products_urls.register('Products', ProductView, basename='Products')
products_urls.register('ProductType', ProductTypeView, basename='ProductType')

