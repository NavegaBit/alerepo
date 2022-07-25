from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'
    icon_name = 'person'
    label = 'Users'
    verbose_name = _('Usuarios')
    verbose_name_plural = _('Usuarios')

    # def ready(self):
    #     from .models import UserProfile
    #     UserProfile.objects.all().delete()
