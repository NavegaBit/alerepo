from django.utils.translation import ugettext_lazy as _


DATES_NUMBER_LIST = ['exact', 'iexact', 'gt', 'gte', 'lt', 'lte']
LETTER_LIST = ['exact', 'iexact', 'contains', 'startswith', 'endswith', 'icontains', 'istartswith', 'iendswith']


class Messages:
    """
    mensajes para esta aplicación, ya sea para errores u otras.
    """
    DATE_NOT_IN_PAST = {"message": _("Esta fecha no esta en pasado"),
                        "code": "date_not_in_past"}
    NOT_VALID_DATE = {"message": _("Esta fecha no es una fecha válida"),
                      "code": "not_valid_date"}
    NOT_VALID_PHONE = {"message": _("este no es un numero de teléfono válido"),
                       "code": "not_valid_phone"}
    REPEATED_PHONE = {"message": _("Este teléfono ya esta en uso"),
                      "code": "not_valid_phone"}
    REPEATED_USERNAME = {"message": _("Este nombre de usuario ya esta en uso"),
                         "code": "not_valid_phone"}
    REPEATED_EMAIL = {"message": _("Este correo electrónico ya esta en uso"),
                      "code": "not_valid_phone"}
