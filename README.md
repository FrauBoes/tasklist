# COMP41110 Task List

A simple Django app built with the Django [getting-started-with-python](https://github.com/heroku/python-getting-started) template, for more details see [Heroku Getting started with Python](https://devcenter.heroku.com/articles/getting-started-with-python).


## Running Locally

Make sure you have the following installed:
Python 3.7 [installed locally](http://install.python-guide.org)
and virtualenv [installed locally](https://virtualenv.pypa.io/en/latest/installation/)

Unzip the source code.

```sh
$ cd tasklist2

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
