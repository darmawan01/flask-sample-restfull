# Example Flask Restful

Sample APi - Base flask-restful ( python )

# Features Available

* **CRUD API**
* **BasicAuthentication**
* **Add User Authentication**
* **and others**

# Installation

    $ clone this repository
    $ cd into that folder

Create a virtual environment

    $ python3 -m venv .venv
    or
    $ virtualenv -p python3 env

Execute to activate the virtual environment

    $ source .venv\bin\activate
    or
    $ source env/bin/activate

Install the requirements

    $ pip3 install -r requirements.txt
    or
    $ pip install -r requrements.txt

# Create Tables

init

    $ python3 manage.py db init

Migrate

    $ python3 manage.py db migrate

Upgrade

    $ python3 manage.py db upgrade

Run the API

    $ Python3 main.py
# Route
    - localhost:5000/auth => set username and password in body
    - localhost:5000/post/1 => method get for get one of post
    - localhost:5000/post/1 => method put for update
    - localhost:5000/post/1 => method deleted for delete
    
# How to Deploy

install gunicorn and change Debug is False

    $ pip3 install gunicorn

run gunicorn

    $ gunicorn --bind 0.0.0.0:8000 main:app
   
  
