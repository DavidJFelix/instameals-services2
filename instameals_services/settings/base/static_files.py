import os

from .base import BASE_DIR

STATICFILES_DIRS = (
)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '../../static')
