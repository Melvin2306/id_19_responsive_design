# Cashflow Board Game - Companion App
---
## Table of contents
* [General info](#general-info)
* [Features](#features)
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

>As a user, I want to add new accounts and be able to change them (mistakes, new information).

>As a user, I want to change my address and be able to send emails to the support teams of the accounts automatically.

### Nice-to-have features

* print out a letter which I'm able to send directly to the account team
* signing in through google
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