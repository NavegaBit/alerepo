from django.db import models

from ..product.models import Product
from ..nomenclator.models import Coin
from ..report.models import ReportPaymentProduct, ReportPaymentYear, ReportPaymentMounth

from django.utils.translation import gettext_lazy as _


class PayState(models.Model):
    """
        Tabla para almacenar los estados de los pagos
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    active = models.BooleanField(_('Activo'), default=True)
    created_at = models.DateTimeField(
        _('Fecha de creado'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('Fecha de modificado'),
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Estado del Pago')
        verbose_name_plural = _('Estado de los pagos')


class Gateway(models.Model):
    """
        Tabla para guardar las configuraciones de los metodos de pago
        """
    coin = models.ManyToManyField(
        Coin,
        related_name="gatewayCoins",
        verbose_name="Moneda",
        default=""
    )
    name = models.CharField(_('Nombre'), max_length=70, default="")
    secret_key = models.CharField(_('Clave secreta'), max_length=1024, default="")
    user_code = models.CharField(_('Código de usuario'), max_length=1024, default="")
    ecommerce_code = models.CharField(_('Código de comercio'), max_length=50, default="")
    first = models.BooleanField(_('Primero'), default=False)
    cards = models.BooleanField(_('Targetas de pago'), default=True)
    charge = models.FloatField(_('Porciento de recargo'), default=1)
    url = models.CharField(_('URL'), max_length=256, default="")
    url_response = models.CharField(_('URL de respuesta'), max_length=256, default="")
    description = models.TextField(_('Descripción'), max_length=2048, default="", blank=True)
    active = models.BooleanField(_('Activo'), default=True)
    created_at = models.DateTimeField(
        _('Fecha de creado'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('Fecha de modificado'),
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Pasarela')
        verbose_name_plural = _('Pasarelas')


class Payment(models.Model):
    """
        Tabla de pagos para la relacion entre los pagos.
        """
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        related_name="ProductTypes",
        verbose_name="Producto",
        default=""
    )

    state = models.ForeignKey(
        PayState,
        on_delete=models.RESTRICT,
        related_name="PayStates",
        verbose_name="Estado del pago",
        default=""
    )

    gateway = models.ForeignKey(
        Gateway,
        on_delete=models.RESTRICT,
        related_name="Gateway",
        verbose_name="Pasarela de pago",
        default=""
    )

    serialized = models.JSONField(_('Serializado de datos'))
    coin = models.ForeignKey(
        Coin,
        on_delete=models.RESTRICT,
        related_name="Coin",
        verbose_name="Monedas",
        default=""
    )
    neto = models.FloatField(_('Neto'), default=0.00)
    total = models.FloatField(_('Total'), default=0.00)
    created_at = models.DateTimeField(
        _('Fecha de pago'),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _('Fecha de modificado'),
        auto_now=True
    )

    def __str__(self):
        return "{}".format(self.product)

    class Meta:
        verbose_name = _('Pago')
        verbose_name_plural = _('Pagos')
