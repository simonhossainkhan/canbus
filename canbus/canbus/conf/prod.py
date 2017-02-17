from base import *
from ..secrets import prod_db

HOST_NAME = "http://desibazaar.pythonanywhere.com/"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': prod_db.get("name"),
        'USER': prod_db.get("user"),
        'PASSWORD': prod_db.get("pass"),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
