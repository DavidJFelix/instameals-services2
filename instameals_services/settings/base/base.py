import os

import dj_database_url
from decouple import config
from django.utils.crypto import get_random_string

# The base directory of the applictaion, used in many configs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The secret key is used for cookie signing and csrf prevention
# In production it should be set in config to prevent logging people out
# It can reasonably be generated every run at a minor inconvenience.
SECRET_KEY = config(
        'SECRET_KEY',
        default=get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'),
)

# Whether or not errors will show stack traces in the browser
# This is off by default and should be off in production. It can be turned on
# for local/development
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ()
ROOT_URLCONF = 'instameals_services.urls'
WSGI_APPLICATION = 'instameals_services.wsgi.application'
DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}
