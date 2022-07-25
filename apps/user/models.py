from datetime import datetime, timedelta


from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.nomenclator.models import Municipality, Location, Country
from apps.reuse.class_view import ImageFieldShow


class UserManagement(AbstractUser):
    username = models.CharField(_('Nombre de usuario'), max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_('Correo'), unique=True)
    phone_no = models.CharField(_('Número de teléfono'), max_length=10, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')


class Contract(models.Model):
    name = models.CharField(max_length=20, default="", blank=True)
    price = models.FloatField(default=1)
    time_in_days = models.IntegerField(default=1)

    def __str__(self):
        return "{} - {}".format(self.name, self.price)

    class Meta:
        verbose_name = _('Tiempo')
        verbose_name_plural = _('Tiempo de Contratos')


class ContractUser(models.Model):
    user = models.ForeignKey(UserManagement, related_name='UserContract', on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, related_name='Contracts', on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        _('Fecha Inicio'),
        auto_now_add=True,
    )
    end_date = models.DateTimeField(
        _('Fecha Final'),
        blank=False
    )

    def __str__(self):
        return "{} - {}: {}".format(self.user, self.contract, self.end_date)

    class Meta:
        verbose_name = _('Contrato')
        verbose_name_plural = _('Asignación de Contratos')


class UserProfile(models.Model, ImageFieldShow):
    OPTIONS = (
        ('M', _('M')),
        ('F', _('F')),
    )
    user = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name=_('Usuario'),
        default=""
    )
    belong_to = models.ForeignKey(
        UserManagement,
        on_delete=models.CASCADE,
        related_name='belong_to',
        verbose_name=_('Usuario de'),
        default=""
    )
    image = models.ImageField(
        _("Foto de perfil"),
        upload_to='photos',
        blank=True,
        null=True,
        default=None
    )
    distribution = models.CharField(_('Reparto'), max_length=120, blank=True, default="")
    sex = models.CharField(_('Sexo'), choices=OPTIONS, max_length=120, default="", blank=True)
    birth = models.DateField(
        _('Fecha de nacimiento'),
        auto_now_add=True,
        blank=True
    )

    # def clean_birth(self, value):
    #     compare_day = datetime.date.today() - timedelta(days=365*15)
    #     if value <= compare_day:
    #         raise ValidationError('The date must be valid...')
    #     return value

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfiles')
        unique_together = ['user', 'belong_to']

