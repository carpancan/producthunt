# Product Hunt with Django 2.2

Is an fullstack project example with Django and html templates.

# INSTALL PROJECT

## PREPARE VIRTUALENV
* virtualenv producthuntvenv
* source producthuntvenv/bin/activate

## CLONE PROJECT
git clone git@github.com:carpancan/producthunt.git

## INSTALL ALL DEPENDENCIES
pip install -r producthunt/requirements.txt

## DATABASE
Database used is postgresql, but you can change by another one

## CREATE SUPERUSER TO START USE WEB PROJECT
* cd producthunt
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py collectstatic (write yes to all questions)

# RUN PROJECT
python manage.py runserver

# COMMANDS
python manage.py

Available subcommands:

### [auth]
    * changepassword
    * createsuperuser

### [contenttypes]
    * remove_stale_contenttypes

### [django]
    * check
    * compilemessages
    * createcachetable
    * dbshell
    * diffsettings
    * dumpdata
    * flush
    * inspectdb
    * loaddata
    * makemessages
    * makemigrations
    * migrate
    * sendtestemail
    * shell
    * showmigrations
    * sqlflush
    * sqlmigrate
    * sqlsequencereset
    * squashmigrations
    * startapp
    * startproject
    * test
    * testserver

### [sessions]
    * clearsessions

### [staticfiles]
    * collectstatic
    * findstatic
    * runserver
