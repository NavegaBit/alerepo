from django.contrib import admin
from django.db.models import Q

from .models import Details, Offerts, StopSaleRangeDate, Season, Product, Price, ProductType, PropertyType, Image, \
    Amenities, ProductDetails

from .resources import OffertsResources, StopSaleRangeDateResources, SeasonResources, ProductResources, \
    PriceResources, ProductTypeResources, PropertyTypeResources, ImageResources, AmenitiesResources,\
    DetailsResources, ProductDetailsResources
from import_export.admin import ImportExportModelAdmin

from apps.user.models import UserProfile


class BelongTo:
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(product__belong_to=request.user.id) | Q(product__belong_to__in=users_profiles))


@admin.register(ProductDetails)
class ProductDetailsPanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('cant', 'product', 'details')
    search_fields = ['cant', 'product__name', 'details__name']
    list_filter = ['active', 'product__name', 'details__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = ProductDetailsResources
    list_per_page = 25
    #
    # def render_change_form(self, request, context, *args, **kwargs):
    #
    #     form_instance = context['adminform'].form
    #     form_instance.fields['email'].widget.attrs['placeholder'] = request.user.email
    #     if not request.user.is_superuser:
    #         users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
    #         form_instance.fields['belong_to'].queryset = form_instance.fields['belong_to'].queryset.filter(
    #             Q(belong_to=request.user.id) | Q(belong_to__in=users_profiles)
    #         )
    #
    #     return super().render_change_form(request, context, *args, **kwargs)


class GroupProductType(admin.TabularInline):
    model = ProductType


@admin.register(Details)
class DetailsPanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('name', 'image_tag')
    search_fields = ['name']
    list_filter = ['active']
    readonly_files = ('image_tag', 'created_at')
    filter_horizontal = ()
    fieldsets = ()
    resources = DetailsResources
    list_per_page = 25


@admin.register(Offerts)
class OffertsPanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('name', 'product', 'price', 'image_tag', 'start_at', 'finish_at')
    search_fields = ['name', 'price', 'product__name']
    list_filter = ['active', 'product__name']
    readonly_files = ('image_tag', 'created_at')
    filter_horizontal = ()
    fieldsets = ()
    resources = OffertsResources
    list_per_page = 25


@admin.register(Product)
class ProductPanelFilter(ImportExportModelAdmin):
    list_display = (
        'name',
        'municipality',
        'belong_to',
        'active',
        'image_tag',
    )
    search_fields = [
        'name',
        'municipality__name',
        'address',
        'description',
        'belong_to__email',
        'meta_text'
    ]
    list_filter = ['active', 'product_type', 'municipality__name']
    readonly_files = ('image_tag', 'created_at', 'belong_to')
    filter_horizontal = ()
    fieldsets = ()
    resources = ProductResources
    list_per_page = 25

    def render_change_form(self, request, context, *args, **kwargs):

        form_instance = context['adminform'].form
        form_instance.fields['email'].widget.attrs['placeholder'] = request.user.email
        if not request.user.is_superuser:
            users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
            form_instance.fields['belong_to'].queryset = form_instance.fields['belong_to'].queryset.filter(
                Q(belong_to=request.user.id) | Q(belong_to__in=users_profiles)
            )

        return super(ProductPanelFilter, self).render_change_form(request, context, *args, **kwargs)

    def get_queryset(self, request):
        qs = super(ProductPanelFilter, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(belong_to=request.user.id) | Q(belong_to__in=users_profiles))


@admin.register(Amenities)
class AmenitiesPanelFilter(ImportExportModelAdmin):
    list_display = (
        'name',
        'description',
        'ico',
        'image',
        'image_tag',
        'active',
        'created_at'
    )
    search_fields = [
        'name',
        'description',
        'active',
        'created_at'
    ]
    list_filter = ['active']
    readonly_files = ('image_tag', 'created_at')
    filter_horizontal = ()
    fieldsets = ()
    resources = AmenitiesResources
    list_per_page = 25


@admin.register(ProductType)
class ProductTypePanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'active', 'created_at')
    search_fields = ['name']
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = ProductTypeResources
    list_per_page = 25


@admin.register(PropertyType)
class PropertyTypePanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'active', 'created_at')
    search_fields = ['name']
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = PropertyTypeResources
    list_per_page = 25


@admin.register(Image)
class ImagePanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('name', 'product', 'image', 'image_tag', 'created_at')
    search_fields = ['name', 'product__name']
    list_filter = ['active', 'product__name']
    readonly_files = ('image_tag', 'created_at')
    filter_horizontal = ()
    fieldsets = ()
    icon_name = 'image'
    resources = ImageResources
    list_per_page = 25


@admin.register(Season)
class SeasonPanelFilter(ImportExportModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'active', 'created_at')
    search_fields = ['name']
    list_filter = ['active']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = SeasonResources
    list_per_page = 25


@admin.register(StopSaleRangeDate)
class StopSaleRangeDatePanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('product', 'start_date', 'end_date', 'created_at')
    search_fields = ['product__name']
    list_filter = ['product__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = StopSaleRangeDateResources
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(product__belong_to=request.user.id) | Q(product__belong_to__in=users_profiles))


@admin.register(Price)
class PricePanelFilter(ImportExportModelAdmin, BelongTo):
    list_display = ('product', 'season', 'amount', 'created_at', 'updated_at')
    search_fields = ['product__name', 'season__name', 'amount']
    list_filter = ['product__name']
    readonly_files = 'created_at'
    filter_horizontal = ()
    fieldsets = ()
    resources = PriceResources
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(Q(product__belong_to=request.user.id) | Q(product__belong_to__in=users_profiles))
