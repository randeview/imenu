#!/bin/sh
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:80