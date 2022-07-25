from .base import *


ALLOWED_HOSTS = env("ALLOWED_HOSTS", default=["*"])
SECRET_KEY = env("SECRET_KEY", default='django-insecure-fdyj@-3xprtum1uw2rc3%pdrf5=-pg$@^nf6n1v-1k%a2t=6in')
DEBUG = env("DEBUG", default=True)

DEFAULT_FILE_STORAGE = env.str("DJANGO_DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage")

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

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

# Anothers Apps

ANOTHER_APPS = [
    'django_extensions',
]

INSTALLED_APPS += ANOTHER_APPS
