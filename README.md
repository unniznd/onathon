# OnamBoard

This webapp can be used as score board for smaller programs

## Team members

[Aanand S](https://www.github.com/unniznd/)


## How it Works

* Create a room 
* Add person to that room
* Update score when necessary
* Send link to others for view of score board

## How to Run locally

* Clone the repo
* Install the requirements ``` pip install -r requirements.txt ```
* Create a file ```dev_settings.py``` in ```onathon``` folder with suitable variables

Model of ```dev_settings.py```
```
ALLOWED_HOSTS = ['localhost']

SECRET_KEY = 'add_secret_key_here'

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}
```
* Set ``` debug = False ``` in ```twitterapi/settings.py```
* Run the server
```
python manage.py runserver 
```
