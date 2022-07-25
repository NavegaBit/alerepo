from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.report'
    icon_name = 'poll'
    label = 'Reportes'
    verbose_name = _('Reportes')
    verbose_name_plural = _('Reportes')
