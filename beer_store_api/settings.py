import os

import dj_database_url

DEBUG = os.environ.get('DEBUG', True)

SECRET_KEY = os.environ.get('SECRET_KEY', 'not-a-secret')

ALLOWED_HOSTS = [
    '127.0.0.1',
    os.environ.get('HOST', 'localhost')
]

ROOT_URLCONF = 'beer_store_api.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'beer_store_api',
    'land',
    'products',
]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', 'postgres://localhost/beerstore'))
}

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
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

STATIC_URL = '/static/'
