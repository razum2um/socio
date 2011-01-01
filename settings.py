# -*- coding: utf-8 -*-
from manage import rel

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'Asia/Novosibirsk'

LANGUAGE_CODE = 'ru'
FIRST_DAY_OF_WEEK = 1
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

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'openteam.middleware.StripWhitespaceMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
# -----------------
    "openteam.context_processors.static",
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    rel('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
# ----------------
    'sorl.thumbnail',
    'openteam',
# ----------------
    'core',
    'blogs',
    'profiles',
    'comments',
)

AUTH_PROFILE_MODULE = 'profiles.UserProfile'
LOGIN_URL = '/profiles/signin/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/profiles/signout/'


try:
    from local_settings import *
except ImportError:
    pass

