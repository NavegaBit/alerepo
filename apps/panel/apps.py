from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.panel'
    icon_name = 'person'
    label = 'Panel'
    verbose_name = _('Panel')
    verbose_name_plural = _('Panel')
