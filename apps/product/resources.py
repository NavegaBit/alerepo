from .models import Offerts, Details, StopSaleRangeDate, Season, Product, Price, ProductType, PropertyType, Image, \
    Amenities, ProductDetails
from import_export import resources


class ProductDetailsResources(resources.ModelResource):
    class Meta:
        model = ProductDetails


class DetailsResources(resources.ModelResource):
    class Meta:
        model = Details


class OffertsResources(resources.ModelResource):
    class Meta:
        model = Offerts


class StopSaleRangeDateResources(resources.ModelResource):
    class Meta:
        model = StopSaleRangeDate


class SeasonResources(resources.ModelResource):
    class Meta:
        model = Season


class ProductResources(resources.ModelResource):
    class Meta:
        model = Product


class PriceResources(resources.ModelResource):
    class Meta:
        model = Price


class ProductTypeResources(resources.ModelResource):
    class Meta:
        model = ProductType


class PropertyTypeResources(resources.ModelResource):
    class Meta:
        model = PropertyType


class ImageResources(resources.ModelResource):
    class Meta:
        model = Image


class AmenitiesResources(resources.ModelResource):
    class Meta:
        model = Amenities
