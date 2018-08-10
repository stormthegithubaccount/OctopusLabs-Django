"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e%kh2#x%jl%ymjx(h458ghti=zi7p^j1kp6_pnpe)s9lp&b9#a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

def get_config(key, default_value=None):
    return os.environ.get(key, default_value)

_ALLOWED_HOSTS = get_config('ALLOWED_HOSTS')

if _ALLOWED_HOSTS is not None:
    ALLOWED_HOSTS = _ALLOWED_HOSTS.split(',')

# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'home.apps.HomeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djstripe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': get_config('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': get_config('DB_HOST'),
        'NAME': get_config('DB_NAME'),
        'USER': get_config('DB_USER'),
        'PASSWORD': get_config('DB_PASSWORD'),
        'PORT': get_config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

if get_config('MEMCACHED_ENABLED') == 'enabled':
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': "%s:%s" % (get_config('MEMCACHED_HOST'), get_config('MEMCACHED_PORT')),
        }
    }
elif get_config('REDIS_ENABLED') == 'enabled':
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': [
                "%s:%s/1" % (get_config('REDIS_MASTER_HOST'), get_config('REDIS_PORT')),
                "%s:%s/1" % (get_config('REDIS_SLAVE_HOST'), get_config('REDIS_PORT')),
            ],
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                'PASSWORD': get_config('REDIS_PASSWORD'),
            },
            'KEY_PREFIX': 'django_redis'
        }
    }


STRIPE_LIVE_PUBLIC_KEY = get_config('STRIPE_LIVE_PUBLIC_KEY', '')
STRIPE_LIVE_SECRET_KEY = get_config('STRIPE_LIVE_SECRET_KEY', '')
STRIPE_TEST_PUBLIC_KEY = get_config('STRIPE_TEST_PUBLIC_KEY', '')
STRIPE_TEST_SECRET_KEY = get_config('STRIPE_TEST_SECRET_KEY', '')
STRIPE_LIVE_MODE = False  # Change to True in production