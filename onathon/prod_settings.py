import os

ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}