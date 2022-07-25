from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.reuse.class_view import ImageFieldShow


class Coin(models.Model):
    """
        Tabla de monedas y cambios monetarios.
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    base = models.BooleanField(_('Base'), default=False)
    first = models.BooleanField(_('Primera elección'), default=False)
    active = models.BooleanField(_('Activo'), default=True)
    value_change = models.FloatField(_('Valor de cambio'), default=1.00)
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

    def save(self, *args, **kwargs):
        try:
            if self.base:
                Coin.objects.filter(base=True).update(base=False)
            if self.first:
                Coin.objects.filter(first=True).update(first=False)

        except Exception as e:
            print(str(e))
        finally:
            super(Coin, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Moneda')
        verbose_name_plural = _('Monedas')


class Country(models.Model):
    """
        Tabla de paises.
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    iso3 = models.CharField(_('Codigo ISO'), max_length=4)
    iso_numeric = models.IntegerField(_('Codigo ISO numerico'),)
    continent_code = models.CharField(_('Codigo de Continente'), max_length=3)
    currency_code = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
        related_name="coins",
        verbose_name="Moneda",
        default=""
    )
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
        verbose_name = _('Pais')
        verbose_name_plural = _('Paises')


class Location(models.Model):
    """
        Tabla de localizaciones dentro de los paises que pudieran ser provincias o estados.
        """
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="Countries",
        verbose_name="Pais",
        default=""
    )
    name = models.CharField(_('Nombre'), max_length=70, default="")
    description = models.TextField(_('Descripción'), max_length=4096, default="", blank=True)
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
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')


class Municipality(models.Model):
    """
        Municipio que pertenece a una provincia
        """
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="Locations",
        verbose_name="Provincia",
        default=""
    )
    name = models.CharField(_('Nombre'), max_length=70, default="")
    description = models.TextField(_('Descripción'), max_length=4096, default="", blank=True)
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
        verbose_name = _('Municipio')
        verbose_name_plural = _('Municipios')


class Place(models.Model, ImageFieldShow):
    """
        Lugar o direccion de interes dentro de un municipio.
        """
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.CASCADE,
        related_name="PlaceMunicipality",
        verbose_name="Municipio",
        default=""
    )
    OPTIONS = (
        ('North', 'Norte'),
        ('Sur', 'Sur'),
        ('East', 'Este'),
        ('West', 'Oeste'),
    )
    name = models.CharField(_('Nombre'), max_length=70, default="", blank=False)
    image = models.FileField(
        _("Imagen"),
        upload_to='places',
        blank=True,
        null=True,
        default=None
    )
    distribution = models.CharField(_('Distribución'), max_length=100, default="", blank=True)
    direction = models.CharField(_('Dirección'), max_length=4096, default="", blank=False)
    number = models.CharField(_('Numero'), max_length=100, default="", blank=True)
    apto_number = models.CharField(_('Número de apartamento'), max_length=100, default="", blank=True)
    orientation = models.CharField(_('Orientación'), max_length=10, choices=OPTIONS)
    description = models.TextField(_('Descripción'), max_length=4096, default="", blank=True)
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
        verbose_name = _('Lugar')
        verbose_name_plural = _('Lugares')


class Category(models.Model):
    """
        Categoria de lugares.
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    description = models.TextField(_('Descripción'), default="", blank=True)
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
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorias')


class TuristDestination(models.Model, ImageFieldShow):
    """
        Destinos turisticos para visitar.
        """
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="TuristLocation",
        verbose_name="Provincia",
        default=""
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="Category",
        verbose_name="Categoría",
        default=""
    )
    name = models.CharField(_('Nombre'), max_length=70, default="")
    image = models.FileField(
        _("Imagen"),
        upload_to='destinations',
        blank=True,
        null=True,
        default=None
    )
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
        verbose_name = _('Destino')
        verbose_name_plural = _('Destinos Turísticos')


class ConstructState(models.Model):
    """
        Estado de las construccion o lugares que se tienen en venta o para alquiler.
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    description = models.TextField(_('Descripción'), max_length=100, default="", blank=True)
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
        verbose_name = _('Estado')
        verbose_name_plural = _('Estado Constructivo')
