from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db.models import Q

from import_export.admin import ImportExportModelAdmin

from .models import PayState, Gateway, Payment
from .resources import GatewayResources, PayStateResources, PaymentResources

from apps.reuse.class_view import Pagination
from apps.user.models import UserProfile


@admin.register(PayState)
class PayStatePanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at')
    search_fields = ['name', 'created_at', 'updated_at']
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = PayStateResources
    list_per_page = 25


@admin.register(Gateway)
class GatewayPanelFilter(ImportExportModelAdmin):
    list_display = (
        'name',
        'user_code',
        'ecommerce_code',
        'first',
        'cards',
        'charge',
        'url',
        'url_response'
    )
    search_fields = [
        'name',
        'user_code',
        'ecommerce_code',
        'first',
        'cards',
        'charge',
        'url',
        'url_response',
        'created_at',
        'updated_at'
    ]
    list_filter = ['active', 'coin__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = GatewayResources
    list_per_page = 25


@admin.register(Payment)
class PaymentPanelFilter(ImportExportModelAdmin):
    list_display = ('product', 'state', 'gateway', 'total', 'coin', 'product_belong', 'created_at')
    search_fields = ['product__name', 'total', 'coin__name', 'state__name', 'gateway__name', 'created_at', 'updated_at']
    list_filter = ['product__name', 'state__name', 'gateway__name']
    readonly_files = []
    filter_horizontal = ()
    fieldsets = ()
    resources = PaymentResources
    list_per_page = 25

    @display(ordering='product__belong_to', description='Pertenece A')
    def product_belong(self, obj):
        return obj.product.belong_to.username

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(product__belong_to=request.user.id) | Q(product__belong_to__in=users_profiles))
