from .base import *


ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=["*"])
SECRET_KEY = env("SECRET_KEY", default='django-insecure-fdyj@-3xprtum1uw2rc3%pdrf5=-pg$@^nf6n1v-1k%a2t=6in')

DEFAULT_FILE_STORAGE = env.str("DJANGO_DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage")
DB_FILES_AUTO_EXPORT_DB_TO_FS = False
DATABASE_FILES_URL_METHOD = 'URL_METHOD_2'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

if "dropbox" in DEFAULT_FILE_STORAGE.lower():
    DROPBOX_OAUTH2_TOKEN = env.str("DROPBOX_OAUTH2_TOKEN", default="")
    DROPBOX_ROOT_PATH = env.str("DROPBOX_ROOT_PATH", default="/")

DATABASES = {
    'default': {
        'ENGINE': env.str("DJANGO_DB_ENGINE", default='django.db.backends.sqlite3'),
        'NAME': env.str("DJANGO_DB_NAME", default='db.sqlite3'),
    }
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
