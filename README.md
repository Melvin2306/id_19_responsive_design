# Address Changer - CODE Software Engeneering Foundations Web Application
---
## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Setup and Running](#setup)
* [Technologies](#technologies)

## General info
### Problem

When you are moving to a new address you manually need to change your address for all your different accounts. Today we have a lot of different accounts for example:

* bank accounts
* insurance accounts
* subscriptions
* payment accounts
* etc.

Keeping in mind and changing the addresses for these accounts is very annoying and time consuming and most of the time you forget to change at least one address.
### Motivation

Because I moved to Berlin in August 2021 to study at [CODE University](https://code.berlin "CODE University website") I needed to change my address for a lot of accounts which accumulated over the years. 

For me it was - and still is - a huge pain to change my address in all these accounts. I probably have not even changed all my accounts addresses so far.

I wanted to develop a beautiful, responsive and intuitie web app which runs on every browser and operating system and allows the user keep track of all of their accounts and manage their address for these accounts from one app.

### Solution

The app should let the user:
* create their own account
* add their current address
* add new accounts

## Features

### Minimum Viable Product

>As a user, I want to create and, if needed, delete an account.

>As a user, I want to add my address and be able to change the address (correcting mistakes). 

>As a user, I want to add new accounts and be able to change them (mistakes, new information, etc.).

>As a user, I want to change my address and be able to send emails to the support teams of the accounts automatically.

### Nice-to-have features

* print out a letter which I'm able to send directly to the account team
* signing in through Google
* add address with Google Maps API

## Setup

### 1. Install the latest python3 version

You should install a version of python3. On Mac, it should cone pre-installed but you should consider updating if you do not have a version of python3 but python2 (check your version by running `python3 --version` in the command line).

### 2. Create a virtual environment

Because the project will have some required packages like flask and we do not want to interfere with all the packages on your computer, you have to create a virtual environment. Enter `python3 -m venv venv` into the command line.

> Note: It is crucial that you do this step while being in the right directory. This should be a copy of this GitHub repository on your computer.
If you want to run your local flask server, you will need to do that with the virtual environment activated.

To activate your virtual environment, type `source venv/bin/activate` on Mac & Linux.

(Be sure deactivate the virtual environment when you want to use the command line like normal again. Run `deactivate` for that. If the comamnd line doesn't show "(venv)" it means, the environment isn't active.)

### 3. Define environment variables in a .env file

First, create a .env file inside of the directory. In here you have to set some basic variables for your virtual environment to work properly.

Paste these in the .env file and save:

`FLASK_ENV=development`

`DATABASE_URL=sqlite:///database.db`

`FLASK_APP=run.py`

`SECRET_KEY=`

> Important: you need to set a secret key after the equal sign. You can fin random keys [here](https://randomkeygen.com).
### 4. Install all required packages

> Be sure that your virtual environment is activated!
Then run `python -m pip install -r requirements.txt`

This will install all packages that are used in this project automatically. No need to install extra packages.

### 5. Database Setup

You will need to run four commands in your terminal to set up the database and fill it with some initial data for the game:

> Be sure that your virtual environment is activated and you did step 4!
1. `flask db init`
2. `flask db migrate -m 'first migration'`
3. `flask db upgrade`
4. `python -m app.scripts.seed`

### 6. Run the server

Now everything is ready to run:

* Run the server with `flask run`
* Stop the server with the keyboard shortcut ctrl+c

## Technologies
Project is created with:
* alembic: 1.7.7
* attrs: 21.4.0
* click: 8.1.2
* Flask: 2.1.1
* Flask-Login: 0.6.0
* Flask-Migrate: 3.1.0
* Flask-SQLAlchemy: 2.5.1
* gunicorn: 20.1.0
* importlib-metadata: 4.11.3
* iniconfig: 1.1.1
* itsdangerous: 2.1.2
* Jinja2: 3.1.1
* Mako: 1.2.0
* MarkupSafe: 2.1.1
* packaging: 21.3
* pluggy: 1.0.0
* py: 1.11.0
* pyparsing: 3.0.7
* pytest: 7.1.1
* python-dotenv: 0.20.0
* SQLAlchemy: 1.4.34
* tomli: 2.0.1
* Werkzeug: 2.1.1
* zipp: 3.8.0