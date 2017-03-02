from base import *
from ..secrets import prod_db

HOST_NAME = "http://iotcanbus.pythonanywhere.com/"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': prod_db.get("name"),
        'USER': prod_db.get("user"),
        'PASSWORD': prod_db.get("pass"),
        'HOST': prod_db.get("host"),
        'PORT': prod_db.get("port"),
    }
}

STATIC_ROOT = "/home/iotcanbus/canbus/static"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    BASE_DIR + '/static/',
    ]
