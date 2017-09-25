import os
import sys

from os.path import abspath, basename, dirname, join, normpath

# Django root directory path
DJANGO_ROOT_DIR = dirname(dirname(abspath(__file__)))

# Project root directory path
PROJECT_ROOT_DIR = dirname(DJANGO_ROOT_DIR)

# The whole site NAME
SITE_NAME = basename(DJANGO_ROOT_DIR)

# Collect static files here
STATIC_ROOT = join(PROJECT_ROOT_DIR, 'assets', 'static')

# Collect media files here
MEDIA_ROOT = join(PROJECT_ROOT_DIR, 'assets', 'media')

# Template directory path
TEMPLATE_ROOT_DIR = [
    join(PROJECT_ROOT_DIR, 'assets', 'templates')
]

# Add api endpoints to Project path
sys.path.append(normpath(join(PROJECT_ROOT_DIR, 'api')))


# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'rest_framework_swagger',
    'django_filters'
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_ROOT_DIR,
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

# #### REST FRAMEWORK Configuration
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'PAGINATE_BY': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
}
# #### SECURITY CONFIGURATIONS
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd^ke$w^z%w!598@!1h#4um=)yd&^mg!c56+66mei+pzz)9ad_7'
# These persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# #### DJANGO RUNNING CONFIGURATION
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Default wsgi application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# Default root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# Default SITE_ID
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/assets/static/'

# Media files URL
MEDIA_URL = '/assets/media/'

# ######### DEBUG Configuration
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default application USER Model
AUTH_USER_MODEL = "authentication.User"

# Swagger Configuration
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha'
}

# Error Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d| [%(name)s:%(lineno)s] | %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "verbose",
            "filename": os.path.join(PROJECT_ROOT_DIR, "log/{{ project_name }}_info.log"),
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "verbose",
            "filename": os.path.join(PROJECT_ROOT_DIR, "log/{{ project_name }}_errors.log"),
            "maxBytes": 10485760,
            "backupCount": 20,
            "encoding": "utf8"
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'info_file_handler', 'error_file_handler'],
            'propagate': True,
            'level': 'INFO',
        },
        '{{ project_name }}': {
            'handlers': ['error_file_handler'],
            'level': 'ERROR',
        },
    }
}
