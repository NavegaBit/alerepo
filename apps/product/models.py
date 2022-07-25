from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.reuse.class_view import ImageFieldShow
from apps.nomenclator.models import Municipality
from apps.user.models import UserManagement


class ProductType(models.Model):
    """
        Tabla para almacenar los tipos de productos 'Nomenclador de tipos de producto'
        """
    name = models.CharField(_('Nombre'), max_length=50, default="")
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
        verbose_name_plural = _('Categorías de Productos')


class PropertyType(models.Model):
    """
        Tabla para almacenar los tipos de propiedad 'Nomenclador de tipos de propiedad'
        """
    name = models.CharField(max_length=50, default="")
    active = models.BooleanField(default=True)
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
        verbose_name = _('Subcategoría')
        verbose_name_plural = _('Subcategorias de Productos')


class Amenities(models.Model, ImageFieldShow):
    """
        Suplementos de los productos
    """
    name = models.CharField(_('Nombre'), max_length=100, default="")
    price = models.FloatField(_('Precio'), default=0.0, blank=True)
    description = models.TextField(_('Descripción'), max_length=2048, default="", blank=True)
    ico = models.FileField(
        _("Icono"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    image = models.FileField(
        _("Imagen"),
        upload_to='photos',
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
        verbose_name = _('Suplemento')
        verbose_name_plural = _('Suplementos')


class Product(models.Model, ImageFieldShow):
    """
        Tabla de productos (Articulos y Servicios).
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    belong_to = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name="ProductB",
        verbose_name=_('Pertenece A'),
        default="",
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        related_name="ProductType",
        verbose_name=_('Tipos de producto'),
        default=""
    )
    property_type = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE,
        related_name="PropertyType",
        verbose_name=_('Tipos de propiedad'),
        default="")
    amenities = models.ManyToManyField(Amenities, verbose_name=_('Suplemento'), blank=True)
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.CASCADE,
        related_name="Municipality",
        verbose_name=_('Municipio'),
        default=""
    )
    release = models.IntegerField(_('Dias para la venta'), default=0)
    address = models.TextField(_('Dirección'), max_length=4096, default="", blank=True)
    email = models.EmailField(_('Correo'), blank=True, default="")
    image = models.FileField(
        _("Imagen"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    active = models.BooleanField(_('Activo'), default=True)
    description = models.TextField(_('Descripción'), max_length=4096, default="", blank=True)
    meta_text = models.TextField(_('SEO'), max_length=2048, default="", blank=True)
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
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')


class Car(models.Model):
    """
        Tabla para almacenar los productos del carrito de compra
        """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="Car",
        verbose_name=_('Producto'),
        default=""
    )
    serialized = models.TextField(max_length=4096, default="")
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
        return "Producto: {0}, {1}".format(self.product, self.created_at)

    class Meta:
        verbose_name = _('Carrito')
        verbose_name_plural = _('Carrito Compra')


class Image(models.Model, ImageFieldShow):
    """
        Tabla para almacenar imagenes secundarias del producto
        """
    name = models.CharField(_('Nombre'), max_length=70, default="", blank=True, null=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="Image",
        verbose_name=_('Producto'),
        default=""
    )
    active = models.BooleanField(_('Activo'), default=True)
    image = models.FileField(
        _("Imagen"),
        upload_to='images',
        blank=False,
        null=False,
        default=None
    )
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
        return "Imagen: {0}, Producto: {1}".format(self.name, self.product)

    class Meta:
        verbose_name = _('Imagen')
        verbose_name_plural = _('Imagenes')


class Details(models.Model, ImageFieldShow):
    """
        Tabla para almacenar detalles de los productos personalizados
        """
    name = models.CharField(_('Nombre'), max_length=70, default="", blank=True, null=True)
    product_type = models.ManyToManyField(
        ProductType,
        related_name="ProductDetails",
        verbose_name=_('Categoría'),
        default=""
    )
    image = models.FileField(
        _("Icon"),
        upload_to='images',
        blank=False,
        null=False,
        default=None
    )
    description = models.CharField(_('Descripción'), max_length=70, default="", blank=True, null=True)
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
        return "{}".format(self.name)

    class Meta:
        verbose_name = _('Detalle')
        verbose_name_plural = _('Detalles')


class ProductDetails(models.Model, ImageFieldShow):
    """
        Tabla para almacenar detalles de los productos personalizados
        """
    cant = models.IntegerField(_('Cantidad'), default=1)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="ProductDetails",
        verbose_name=_('Producto'),
        default=""
    )
    details = models.ForeignKey(
        Details,
        on_delete=models.CASCADE,
        related_name="Detail",
        verbose_name=_('Details'),
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
        return "{}-{}".format(self.product, self.details)

    class Meta:
        verbose_name = _('Detalle')
        verbose_name_plural = _('Detalles del producto')


class Offerts(models.Model, ImageFieldShow):
    """
        Tabla para almacenar ofertas de los productos
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="Oferts",
        verbose_name=_('Productos'),
        default=""
    )
    image = models.FileField(
        _("Imagen"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    price = models.FloatField(_('Precio'), default=0.0, blank=True)
    description = models.TextField(_('Descripción'), default="", blank=True)
    active = models.BooleanField(_('Activo'), default=True)
    start_at = models.DateTimeField(
        _('Fecha de Inicio'),
    )
    finish_at = models.DateTimeField(
        _('Fecha Fin'),
    )
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
        return "Imagen: {0}, Producto: {1}".format(self.name, self.product)

    class Meta:
        verbose_name = _('Oferta')
        verbose_name_plural = _('Ofertas')


class Season(models.Model):
    """
        Tabla para relacionar las temporadas de los productos
        """
    name = models.CharField(_('Nombre'), max_length=70, default="")
    active = models.BooleanField(_('Activo'), default=True)
    start_date = models.DateTimeField(_('Fecha inicio'))
    end_date = models.DateTimeField(_('Fecha final'))
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
        return "Inicio: {0}, Fin: {1} -> Temporada: {2}".format(self.start_date, self.end_date, self.name)

    class Meta:
        verbose_name = _('Temporada')
        verbose_name_plural = _('Temporadas')


class StopSaleRangeDate(models.Model):
    """
        Tabla para relacionar los paros de venta en los productos
        """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="ProductoStopSaleRangeDate",
        verbose_name=_('Producto'),
        default=""
    )
    active = models.BooleanField(_('Activo'), default=True)
    start_date = models.DateTimeField(_('Fecha inicio'))
    end_date = models.DateTimeField(_('Fecha final'))
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
        return "Inicio: {0}, Fin: {1} -> Producto: {2}".format(self.start_date, self.end_date, self.product)

    class Meta:
        verbose_name = _('Paro')
        verbose_name_plural = _('Paros de Venta')


class Price(models.Model):
    """
        Precio de los productos
    """
    amount = models.FloatField(_('Precio'), default=0.0)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='Product',
        verbose_name=_('Producto'),
        default=""
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='Season',
        verbose_name='Temporada',
        default="")
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
        return "{}: {}".format(self.product, self.amount)

    class Meta:
        verbose_name = _('Precio')
        verbose_name_plural = _('Precios de Producto')
