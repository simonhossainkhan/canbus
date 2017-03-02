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

STATIC_ROOT = "/home/skhan/School Projects/canbus_service/static"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    BASE_DIR + '/static/',
]
