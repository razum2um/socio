# -*- coding: utf-8 -*-
import settings
# set SMTP hostname here
EMAIL_HOST = None
INTERNAL_IPS = ('127.0.0.1',)

SERVER_EMAIL = '<no-reply@localhost>'
DEFAULT_FROM_EMAIL = '<webmaster@localhost>'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ':memory:',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ADMINS = (
    ('Administrator', 'test@example.com'),
)

SECRET_KEY = 'a09d7fbk2j3hfnapd8fay3fkabmnefb,m32bmn23kf23fh23f'

if settings.DEBUG:
    CACHE_BACKEND = 'dummy://'
    CACHE_MIDDLEWARE_SECONDS = 0
    INSTALLED_APPS = settings.INSTALLED_APPS + (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

else:
    MIDDLEWARE_CLASSES = (
        'django.middleware.cache.UpdateCacheMiddleware',
    ) + MIDDLEWARE_CLASSES + (
        'django.middleware.http.ConditionalGetMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware'
    )
    CACHE_BACKEND = 'file:///tmp/django_cache'
    CACHE_MIDDLEWARE_SECONDS = 2400

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MANAGERS = ADMINS

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

