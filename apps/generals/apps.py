from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GeneralsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.generals'
    icon_name = 'business'
    label = 'Empresa'
    verbose_name = _('Empresa')
    verbose_name_plural = _('Empresa')