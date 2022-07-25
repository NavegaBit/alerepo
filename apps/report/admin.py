from django.contrib import admin
from django.db.models import Q

from datetime import datetime
import calendar

from .models import ReportPaymentYear, ReportPaymentMounth, ReportPaymentProduct
from apps.user.models import UserProfile

from admincharts.admin import AdminChartMixin


class ChangueAdminChart(AdminChartMixin):
    request = object

    def changelist_view(self, request, extra_context=None):
        self.request = request
        response = super().changelist_view(request, extra_context=extra_context)

        # This could be a redirect and not have context_data
        if not hasattr(response, "context_data"):
            return response

        if "cl" in response.context_data:
            changelist = response.context_data["cl"]
            chart_queryset = self.get_list_chart_queryset(changelist)
            response.context_data["adminchart_queryset"] = chart_queryset
            response.context_data[
                "adminchart_chartjs_config"
            ] = self.get_list_chart_config(chart_queryset)
        else:
            response.context_data["adminchart_queryset"] = None
            response.context_data["adminchart_chartjs_config"] = None

        return response


@admin.register(ReportPaymentMounth)
class ReportPaymentMounthAccountAdmin(ChangueAdminChart, admin.ModelAdmin):
    list_display = ('user', 'year', 'mounth', 'total')
    search_fields = []
    list_filter = []
    filter_horizontal = ()
    fieldsets = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(user__id__in=users_profiles)

    def get_list_chart_data(self, queryset):
        if not queryset:
            return {}

        labels = []
        totals = []

        current_year = datetime.now().year
        queryset = ReportPaymentMounth.objects.filter(year=current_year, user=self.request.user).order_by('mounth')
        for x in queryset:
            labels.append(calendar.month_name[int(x.mounth)].upper()+'-'+str(x.year))
            totals.append(x.total)

        return {
            "labels": labels,
            "datasets": [
                {"label": "Ventas por Mes", "data": totals, "backgroundColor": "#79aec8"},
            ],
        }


@admin.register(ReportPaymentYear)
class ReportPaymentYearAccountAdmin(ChangueAdminChart, admin.ModelAdmin):
    list_display = ('user', 'year', 'total')
    search_fields = []
    list_filter = []
    filter_horizontal = ()
    fieldsets = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(user__id__in=users_profiles)

    def get_list_chart_data(self, queryset):
        if not queryset:
            return {}

        labels = []
        totals = []

        current_year = datetime.now().year
        queryset = ReportPaymentYear.objects.filter(year__gte=current_year-5, user=self.request.user).order_by(
            'year')
        for x in queryset:
            labels.append(x.year)
            totals.append(x.total)

        return {
            "labels": labels,
            "datasets": [
                {"label": "Ventas por Año", "data": totals, "backgroundColor": "#79aec8"},
            ],
        }


@admin.register(ReportPaymentProduct)
class ReportPaymentProductAccountAdmin(ChangueAdminChart, admin.ModelAdmin):
    list_display = ('user', 'product_type', 'total')
    search_fields = []
    list_filter = []
    filter_horizontal = ()
    fieldsets = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        users_profiles = UserProfile.objects.filter(belong_to=request.user.id).values('user__id')
        return qs.filter(user__id__in=users_profiles)

    def get_list_chart_data(self, queryset):
        if not queryset:
            return {}

        labels = []
        totals = []

        queryset = ReportPaymentProduct.objects.filter(user=self.request.user)
        for x in queryset:
            labels.append(str(x.product_type))
            totals.append(x.total)

        return {
            "labels": labels,
            "datasets": [
                {"label": "Ventas por Producto", "data": totals, "backgroundColor": "#79aec8"},
            ],
        }
