from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payment'
    icon_name = 'monetization_on'
    label = 'Payments'
    verbose_name = _('Pagos')
    verbose_name_plural = _('Pagos')

    def ready(self):
        import apps.payment.signals
