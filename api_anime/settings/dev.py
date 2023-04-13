from api_anime.settings import *


DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CREATED_APPS = [
    'anime',
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
}
