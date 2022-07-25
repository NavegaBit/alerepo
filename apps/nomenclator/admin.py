from django.contrib import admin
from .models import Coin, Country, Location, Place, TuristDestination, ConstructState, Municipality, Category
from .resources import CoinResources, CountryResources, LocationResources, PlaceResources, \
    TuristDestinationResources, MunicipalityResources, CategoryResources
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ['name', 'description']
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = CategoryResources
    list_per_page = 25


@admin.register(Coin)
class CoinPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'base', 'first', 'active', 'created_at')
    search_fields = ['name']
    list_filter = ['base', 'first', 'active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = CoinResources
    list_per_page = 25


@admin.register(Country)
class CountryPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'iso3', 'iso_numeric', 'continent_code', 'currency_code', 'active')
    search_fields = ['name', 'iso3', 'iso_numeric', 'currency_code__name']
    list_filter = ['continent_code', 'active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = CountryResources
    list_per_page = 25


@admin.register(Location)
class LocationPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'country', 'created_at', 'active')
    search_fields = ['name', 'country__name']
    list_filter = ['active', 'country__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = LocationResources
    list_per_page = 25


@admin.register(Municipality)
class MunicipalityPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'location', 'created_at', 'active')
    search_fields = ['name', 'location__name']
    list_filter = ['active', 'location__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = MunicipalityResources
    list_per_page = 25


@admin.register(Place)
class PlacePanelFilter(ImportExportModelAdmin):
    list_display = (
        'name',
        'municipality',
        'number',
        'apto_number',
        'image_tag',
        'active'
    )
    search_fields = [
        'name',
        'municipality__name',
        'distribution',
        'direction',
        'number',
        'apto_number',
        'orientation',
        'created_at',
        'active'
    ]
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = PlaceResources
    list_per_page = 25


@admin.register(TuristDestination)
class TuristDestinationPanelFilter(ImportExportModelAdmin):
    list_display = (
        'name',
        'location',
        'image_tag',
        'created_at',
        'active'
    )
    search_fields = [
        'name',
        'location__name',
        'created_at',
        'active'
    ]
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = TuristDestinationResources
    list_per_page = 25