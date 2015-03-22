#!/bin/bash
clear
echo "migrating"
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py syncdb 
