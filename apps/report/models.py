from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.product.models import ProductType
from apps.user.models import UserManagement


class ReportPaymentMounth(models.Model):

    user = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name="ReportMounth",
        verbose_name=_('Pertenece A'),
        default="",
    )
    year = models.IntegerField(_('Year'), default="")
    mounth = models.IntegerField(_('Mes'), default="")
    total = models.FloatField(_('Total'), default="")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def __str__(self):
        return "Año: {} - Mes: {}".format(self.year, self.mounth)

    class Meta:
        verbose_name = _('Ventas')
        verbose_name_plural = _('Ventas por Mes')
        unique_together = ['user', 'year', 'mounth']


class ReportPaymentYear(models.Model):
    user = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name="ReportYear",
        verbose_name=_('Pertenece A'),
        default="",
    )
    year = models.IntegerField(_('Año'), default="")
    total = models.FloatField(_('Total'), default="")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def __str__(self):
        return "Año: {}".format(self.year)

    class Meta:
        verbose_name = _('Ventas')
        verbose_name_plural = _('Ventas por Año')
        unique_together = ['user', 'year']


class ReportPaymentProduct(models.Model):
    user = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name="ReportProduct",
        verbose_name=_('Pertenece A'),
        default="",
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="ProductTypeReport",
        verbose_name=_('Tipos de producto'),
        default=""
    )
    total = models.FloatField(_('Total'), default="")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def __str__(self):
        return "Tipo de producto: {}".format(self.product_type)

    class Meta:
        verbose_name = _('Ventas')
        verbose_name_plural = _('Ventas por Producto')
        unique_together = ['user', 'product_type']
