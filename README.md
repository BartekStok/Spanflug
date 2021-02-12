# Document manage app for SpanFlug


### Used Technologies:

```
$ Python 3.8.5
$ Django
$ SQLlite
```

### Installing

It is best to use the python `virtualenv` tool to build locally:

```sh
$ mkdir app && cd app
$ git clone git@github.com:BartekStok/Spanflug.git
$ cd cd Spanflug
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ generate secret key using 
    python3 manage.py shell
    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()
$ copy generated key and paste it to settings.py
$ python3 manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## License

This project is licensed under the MIT License

- Copyright 2020 © Bartłomiej Stokłosa
