# -*- coding: utf-8 -*-
from manage import rel

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Egor V. Nazarkin', 'nimnull@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'socio.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Novosibirsk'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = rel('media')

MEDIA_URL = '/media/'
STATIC_URL  = MEDIA_URL + 'static/'
CSS_URL     = STATIC_URL + 'css/'
JS_URL      = STATIC_URL + 'js/'
IMG_URL     = STATIC_URL + 'img/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ovt4_#lp7=o)_)20e6r_gvl58%p90)^zcdc6vsd5%e5v3i01lx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'openteam.middleware.StripWhitespaceMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
# -----------------
    "openteam.context_processors.static",
)

ROOT_URLCONF = 'socio.urls'

TEMPLATE_DIRS = (
    rel('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
#    'django.contrib.admin',
# ----------------
    'south',
    'sorl.thumbnail',
    'openteam',
# ----------------
    'core',
    'profiles',
)


if DEBUG:
    CACHE_BACKEND = 'dummy://'
    CACHE_MIDDLEWARE_SECONDS = 0
else:
    CACHE_BACKEND = 'locmem://'
    CACHE_MIDDLEWARE_SECONDS = 3600


AUTH_PROFILE_MODULE = 'profiles.UserProfile'
LOGIN_URL = '/profiles/signin/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/profiles/signout/'

