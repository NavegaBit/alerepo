from import_export import resources
from .models import Coin, Country, Location, Place, TuristDestination, Category, ConstructState, Municipality


class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category


class CoinResources(resources.ModelResource):
    class Meta:
        model = Coin


class CountryResources(resources.ModelResource):
    class Meta:
        model = Country


class LocationResources(resources.ModelResource):
    class Meta:
        model = Location


class PlaceResources(resources.ModelResource):
    class Meta:
        model = Place


class TuristDestinationResources(resources.ModelResource):
    class Meta:
        model = TuristDestination


class ConstructStateResources(resources.ModelResource):
    class Meta:
        model = ConstructState


class MunicipalityResources(resources.ModelResource):
    class Meta:
        model = Municipality
