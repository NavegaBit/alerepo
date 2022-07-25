import datetime
import re

from django.core.validators import ValidationError, RegexValidator

from .constants import Messages


def validate_date_in_past(value):
    """
    funcion para validar que una fecha este en pasado
    :param value: objeto Datetime
    :return: objeto Datetime pasado por parametro
    """
    today = datetime.datetime.today()
    if value.date() >= today.date():
        raise ValidationError(Messages.DATE_NOT_IN_PAST["message"], Messages.DATE_NOT_IN_PAST["code"])
    return value


def valid_phone_string(value):
    """
    función para validar números de teléfonos con las siguientes sintaxis
    0001 12345678
    0053 1234 1234
    +123 123456789
    12345678
    1 (800) 333 3333
    1-(800) 333 3333
    (800)-123-1234
    +53 5323 2345
    +53 1234 1234
    0053 5768 8078
    +53-1234-1234
    123456789
    23 45 90 98
    :param value: cadena de texto con el número de teléfono
    :return: cadena de texto con el número de teléfono
    """
    phone_regex = r"^(\+[1-9]{1,3}|[0][0-9]{1,3}|[0-9]{1,3}|)+([- ]){0,1}"\
                  "([0-9]{8,9}|"\
                  "\([0-9]{3}\)([- ])?[0-9]{3}([- ])?[0-9]{4}|"\
                  "[0-9]{4}([- ])?[0-9]{4}|"\
                  "[0-9]{3}([- ])?[0-9]{3}([- ])?[0-9]{3}|"\
                  "[0-9]{2}[ -]?[0-9]{2}[ -]?[0-9]{2}[ -]?[0-9]{2})$"
    digits = sum(1 for c in value.lstrip('+0') if c.isdigit() or c == "+")
    if not re.match(phone_regex, str(value)):
        raise ValidationError(Messages.NOT_VALID_PHONE["message"], Messages.NOT_VALID_PHONE["code"])
    elif 8 > digits or digits > 11:
        raise ValidationError(Messages.NOT_VALID_PHONE["message"], Messages.NOT_VALID_PHONE["code"])

    return value
