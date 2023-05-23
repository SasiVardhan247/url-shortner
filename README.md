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

<h1 align="center">url-shortner</h1>


## 🔖Steps to Contribute 

Following are the steps to guide you:

* Step 1: Fork the repo and Go to your Git terminal and clone it on your machine.
    ```
    git clone https://github.com/<your_github_username>/url-shortner.git
    ```
* Step 2: Add an upstream link to the main branch in your cloned repo
    ```
    git remote add upstream https://github.com/<your_github_username>/url-shortner.git
    ```
* Step 3: Keep your cloned repo up to date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
    ```
    git pull upstream main
    ```
* Step 4: Create your feature branch (This is a necessary step, so don't skip it)
    ```
    git checkout -b <feature-name>
    ```
* Step 5: Track and stage your changes.
    ```
     # Track the changes
     git status

     # Add changes to Index
     git add .
     ```
* Step 6: Commit all the changes (Write commit message as "Small Message")
    ```
    git commit -m "Write a meaningful but small commit message"
    ```
* Step 7: Push the changes for review
    ```
    git push origin <branch-name>
    ```
* Step 8: Create a PR on Github. (Don't just hit the create a pull request button, you must write a PR message to clarify why and what are you contributing)
