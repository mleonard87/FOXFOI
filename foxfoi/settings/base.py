"""
Django settings for FOXFOI project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'foxfoi')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'foi',
    'mps',
    'keyterms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',
)

LOGIN_REDIRECT_URL = '/foi/'

TEMPLATE_DIRS = [os.path.join(PROJECT_DIR, 'templates')]

STATIC_FOUNDATION = os.path.join(os.path.join(PROJECT_DIR, 'static'), 'foundation')
STATIC_JQUERYUI = os.path.join(os.path.join(PROJECT_DIR, 'static'), 'jquery-ui')
STATIC_APPLICATION = os.path.join(os.path.join(PROJECT_DIR, 'static'), 'application')
STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_FOUNDATION, 'css')),
    ('css', os.path.join(STATIC_FOUNDATION, 'foundation-icons')),
    ('js', os.path.join(STATIC_FOUNDATION, 'js')),
    ('js', os.path.join(STATIC_JQUERYUI, 'js')),
    ('css', os.path.join(STATIC_APPLICATION, 'css')),
    ('js', os.path.join(STATIC_APPLICATION, 'js')),
)

ROOT_URLCONF = 'foxfoi.urls'

WSGI_APPLICATION = 'foxfoi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Canberra'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
