# URL Shortner Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/SasiVardhan247/url-shortner.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
```

If pip doesn't work in Vs-Code use:

```sh
$python3 -m pip install virtualenv
            (or)
$python -m pip install virtualenv
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
And navigate to `https://127.0.0.1:8000/url/shorten/`.
