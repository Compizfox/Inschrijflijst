"""
Django settings for Inschrijflijst project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.contrib.messages import constants as message_constants
from django.utils.translation import ugettext_lazy as _

from .settings_local import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'app.apps.AppConfig',
	'bootstrap3',
	'bootstrap3_datetime',
	'post_office'
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'app.middleware.last_seen_middleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'app.middleware.base_url_middleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'app/templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'app.context_processors.now',
			],
		},
	},
]

WSGI_APPLICATION = 'wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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

AUTH_USER_MODEL = 'app.User'

# Authentication URLs
LOGIN_REDIRECT_URL = FORCE_SCRIPT_NAME + '/'
LOGOUT_REDIRECT_URL = FORCE_SCRIPT_NAME + '/'
LOGIN_URL = FORCE_SCRIPT_NAME + '/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = FORCE_SCRIPT_NAME + '/static/'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
USE_I18N = True
USE_L10N = False
USE_TZ = True
LANGUAGE_CODE = 'NL-nl'

LANGUAGES = [
	('nl', _('Nederlands')),
	('en', _('English')),
]

MESSAGE_TAGS = {
	message_constants.DEBUG:    'alert-danger',
	message_constants.INFO:     'alert-info',
	message_constants.SUCCESS:  'alert-success',
	message_constants.WARNING:  'alert-warning',
	message_constants.ERROR:    'alert-danger'
}

# Django Post Office
EMAIL_BACKEND = 'post_office.EmailBackend'

POST_OFFICE = {
	'BATCH_SIZE': 30
}

# ISO 8601 or GTFO
DATE_FORMAT = 'j F Y'  # '20 januari 2009'
TIME_FORMAT = 'H:i'  # '15:23'
DATETIME_FORMAT = 'j F Y H:i'  # '20 januari 2009 15:23'
MONTH_DAY_FORMAT = 'j F'  # '20 januari'
SHORT_DATE_FORMAT = 'Y-n-j'  # '2009-1-20'
SHORT_DATETIME_FORMAT = 'Y-n-j H:i'  # '2009-1-20 15:23'
FIRST_DAY_OF_WEEK = 1  # Monday

DATE_INPUT_FORMATS = [
	'%Y-%m-%d',  # '2009-1-20'
	'%d-%m-%Y'  # '20-01-2009'
]
TIME_INPUT_FORMATS = [
	'%H:%M:%S',  # '15:23:35'
	'%H:%M:%S.%f',  # '15:23:35.000200'
	'%H:%M'  # '15:23'
]
DATETIME_INPUT_FORMATS = [
	'%Y-%m-%d %H:%M:%S',  # '2006-10-25 14:30:59'
	'%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
	'%Y-%m-%d %H:%M',  # '2006-10-25 14:30'
	'%Y-%m-%d'  # '2006-10-25'
]

THOUSAND_SEPARATOR = ' '
