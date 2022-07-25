import uuid


def scramble_upload(instance, filename, subdirectory=""):
    """
    esta función devuelve una cadena de texto con una ruta para un archivo
    :param instance: instancia de un archivo
    :param filename: nombre de archivo de la instancia
    :param subdirectory: nombre de un subdirectorio para agregar a la ruta generada
    :return: cadena de texto
    """
    ext = filename.split('.')[-1]
    return subdirectory+'/{}.{}'.format(uuid.uuid4(), ext)


def scramble_upload_image(instance, filename):
    """
    esta función devuelve una cadena de texto con una ruta para un archivo de avatar usando la función
    scramble_upload
    :param instance: instancia de un archivo
    :param filename: nombre de archivo de la instancia
    :return:
    """
    return scramble_upload(instance, filename, "/")
