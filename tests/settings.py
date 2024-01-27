import os

DEBUG = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'thisisntactuallysecretatall'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
    'jsignature',
    'tests',
]

PASSWORD_HASHERS = {
    'django.contrib.auth.hashers.MD5PasswordHasher',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
