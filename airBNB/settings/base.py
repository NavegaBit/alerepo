"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import os

import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'. ------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
PORJECT_DIR = BASE_DIR.parent
APPS_DIR = PORJECT_DIR / "apps"

env = environ.Env()

DEBUG = env.bool("DJANGO_DEBUG", False)

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

# Application definition

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])

INSTALLED_APPS = [
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    "django_filters",
    'binary_database_files',
    'import_export',
    'admincharts',
]

LOCAL_APPS = [
    'apps.payment.apps.PaymentConfig',
    'apps.panel.apps.PanelConfig',
    'apps.user.apps.UserConfig',
    'apps.generals.apps.GeneralsConfig',
    'apps.nomenclator.apps.NomenclatorsConfig',
    'apps.product.apps.ProductConfig',
    'apps.report.apps.ReportConfig',
]

INSTALLED_APPS += (THIRD_PARTY_APPS + LOCAL_APPS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'airBNB.urls'

STATIC_URL = 'static/'

WSGI_APPLICATION = 'airBNB.wsgi.application'

# LANGUAGE
LANGUAGE_CODE = 'es-es'

# FILES
DEFAULT_FILE_STORAGE = env.str("DJANGO_DEFAULT_FILE_STORAGE", default="binary_database_files.storage.DatabaseStorage")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATIC FILES
STATIC_ROOT = os.path.join(PORJECT_DIR, "statics")

CORS_ALLOW_ALL_ORIGINS = True

# EXPORT + IMPORT DJANGO DATABASE
IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = True

# CMS DJANGO STYLES
CMS_ENABLE_UPDATE_CHECK = True
CMS_UPDATE_CHECK_TYPE = ('minor')

AUTH_USER_MODEL = 'Users.UserManagement'

