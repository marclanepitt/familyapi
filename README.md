* Api urls, versioning
* secret key
* common app


## Dev setup
* `virtualenv venv -p python3`
* `source venv/bin/activate` or the equivalent on windows
* `pip install -r requirements.txt`
* `ln -s path/to/tutory_api/tutory_api/settings/local_settings.py.dev path/to/tutory_api/tutory_api/settings/local_settings.py`
* `python manage.py migrate`
* `python manage.py runserver`
