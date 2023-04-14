from api_anime.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CREATED_APPS = [
    'anime',
    'users',
]

INSTALLED_APPS += CREATED_APPS

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_PERMISSION_CLASSES': [
        'apps.anime.services.permissions.IsAdminOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}
