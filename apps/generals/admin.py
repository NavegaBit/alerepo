import environ

from .models import CompanyData, SocialNet, Promotion
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

env = environ.Env()


class CompanyResource(resources.ModelResource):
    class Meta:
        model = CompanyData


class SocialNetResource(resources.ModelResource):
    class Meta:
        model = SocialNet


class PromotionResource(resources.ModelResource):
    class Meta:
        model = Promotion


@admin.register(CompanyData)
class CompanyDataPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'email', 'visual', 'image_tag', 'active', 'created_at')
    search_fields = ['name', 'email', 'visual', 'active', 'created_at']
    list_filter = ['active']
    readonly_files = ['created_at', 'image_tag', 'key']
    filter_horizontal = ()
    fieldsets = ()
    resource_class = CompanyResource
    list_per_page = 25


@admin.register(SocialNet)
class SocialNetPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'share', 'image_ico', 'active', 'created_at')
    search_fields = ['name', 'share', 'active', 'created_at']
    list_filter = ['active']
    readonly_files = ['image_ico', 'image_tag', 'created_at']
    filter_horizontal = ()
    fieldsets = ()
    resource_class = SocialNetResource
    list_per_page = 25


@admin.register(Promotion)
class PromotionPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'image_tag', 'active', 'created_at')
    search_fields = ['name', 'active', 'created_at']
    list_filter = ['active']
    readonly_files = ['created_at', 'image_tag']
    filter_horizontal = ()
    fieldsets = ()
    resource_class = CompanyResource
    list_per_page = 25
