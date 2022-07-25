from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product'
    icon_name = 'local_offer'
    label = 'Products'
    verbose_name = _('Productos')
    verbose_name_plural = _('Productos')
