import os

from .settings import *  # noqa: F403

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scratch',
        'USER': 'scratch',
        'PASSWORD': 'scratch',
        'HOST': 'localhost',
        'PORT': '6432',
    }
}
