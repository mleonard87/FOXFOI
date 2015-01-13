"""Production settings and globals."""

from .base import *
from .secrets import get_secret

# No debug for production
if os.environ.get('DEBUG') == 'True':
    DEBUG = True
else:
    DEBUG = False

SECRET_KEY = get_secret('SECRET_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_secret('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_secret('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Allow all hosts
ALLOWED_HOSTS = ['*']

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')