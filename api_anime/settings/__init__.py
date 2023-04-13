from pathlib import Path
from dynaconf import Dynaconf
from anime.services.file_utils import FileValidator

BASE_DIR = Path(__file__).resolve().parent.parent.parent

secrets_data = Dynaconf(
    environments=False,
    settings_file=[BASE_DIR / '.secrets.json']
)

SECRET_KEY = secrets_data.get('SECRET_KEY')

DEBUG = True if secrets_data.get('DEBUG') == '1' else False

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_anime.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'api_anime.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets_data.get('DB_NAME'),
        'USER': secrets_data.get('DB_USER'),
        'PASSWORD': secrets_data.get('DB_PASSWORD'),
        'HOST': secrets_data.get('DB_HOST'),
        'PORT': secrets_data.get('DB_PORT')
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

IMAGE_LIMIT = FileValidator(byte_limit=3)
VIDEO_LIMIT = FileValidator(byte_limit=5120)
