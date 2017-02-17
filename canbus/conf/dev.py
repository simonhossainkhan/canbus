from base import *
from ..secrets import dev_db

HOST_NAME = "http://0.0.0.0:8000/"


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': dev_db.get("name"),
        'USER': dev_db.get("user"),
        'PASSWORD': dev_db.get("pass"),
        'HOST': dev_db.get("host"),
        'PORT': dev_db.get("port"),
    }
}