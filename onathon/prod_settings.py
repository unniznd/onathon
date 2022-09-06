import os
import json

ALLOWED_HOSTS = ['onamboard.herokuapp.com']

with open('secret_key.json') as f:
    secret = json.load(f)
    

SECRET_KEY = os.environ.get('SECRET_KEY')



DATABASES = {
    "default": {
        "ENGINE": secret['ENGINE'],
        "NAME": secret['NAME'],
        "USER": secret['USER'],
        "PASSWORD":os.environ.get('PASSWORD'),
        "HOST":secret['HOST'],
        "PORT": secret['PORT']
    }
}
