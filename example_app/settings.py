#!/usr/local/bin/python
# -*- coding: utf-8 -*- 
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fsch+6!=q+@ol&%0x!nwdl@48^ixbd4clx5f1i!5n^66y+pmn*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'talkingstatues.xyz', u'localhost', u'api.talkingstatues.xyz']


# Application definition

INSTALLED_APPS = (
    'statues.apps.StatuesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'chatterbot.ext.django_chatterbot',
    'example_app',
)

# ChatterBot settings

CHATTERBOT = {
    'name': 'Talking statues chatbot',
    'django_app_name': 'django_chatterbot',
    'filters': 'chatterbot.filters.RepetitiveResponseFilter',
    'storage_adapter': 'chatterbot.storage.DjangoStorageAdapter',
    'database': './db.sqlite3',
    'logic_adapters': [
        'chatterbot.logic.BestMatch',
    ],
    'filters': [
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',    #'trainer': 'chatterbot.trainers.ListTrainer',
    'training_data': [
        'chatterbot.corpus.english.greetings',
        'chatterbot.corpus.english.conversations',
        'chatterbot.corpus.english.history',
        'chatterbot.corpus.english.humor',
        'chatterbot.corpus.english.emotion',
        './statues.corpus.json',
    ],
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'example_app.urls'

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

WSGI_APPLICATION = 'example_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),
)

MEDIA_ROOT = ''
MEDIA_URL = '/pic_folder/'

