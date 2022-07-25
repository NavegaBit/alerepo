from binary_database_files.models import File

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.reuse.class_view import ImageFieldShow


class CompanyData(models.Model, ImageFieldShow):
    """
        Tabla del sistema para establecer caracteristicas generales de la compania
        """
    OPTIONS = (
        ('Dark', 'Oscuro'),
        ('White', 'Claro'),
    )
    name = models.CharField(_('Nombre'), max_length=70, default="")
    email = models.EmailField(_('Correo'), blank=True,  default="")
    ico = models.FileField(
        _("Icono"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    favico = models.FileField(
        _("Favico"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    image = models.FileField(
        _("Logo"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    key = models.CharField(_('Llave'), default="cvk3c8xqtc7jrktrthmxpqkfb", unique=True, max_length=100, editable=False)
    visual = models.CharField(_('Estilo'), max_length=70, choices=OPTIONS)
    active = models.BooleanField(_('Activo'), default=True)
    time_exec = models.TimeField(_(u"Tareas automaticas"), blank=True, default="23:59:12")
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
            if not CompanyData.objects.all():
                super(CompanyData, self).save(*args, **kwargs)
        except Exception as e:
            print(str(e))

    class Meta:
        verbose_name = _('Empresa')
        verbose_name_plural = _('Datos de la Empresa')


class SocialNet(models.Model, ImageFieldShow):
    """
        Tabla del sistema para establecer caracteristicas generales del mismo
        """
    name = models.CharField(_('Nombre'), max_length=70)
    share = models.CharField(_('Compartir'), max_length=2048)
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
        verbose_name = _('Red')
        verbose_name_plural = _('Redes Sociales')


class Promotion(models.Model, ImageFieldShow):
    """
        Tabla del sistema para establecer promociones en el sitio
        """
    name = models.CharField(_('Nombre'), max_length=70)
    description = models.TextField(_('Descripción'), default="", blank=True)
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
        verbose_name = _('Promoción')
        verbose_name_plural = _('Promociones')
