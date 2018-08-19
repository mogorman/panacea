#!/usr/bin/env bash
rm db.sqlite3
rm demographics/migrations/0001_initial.py
rm -rf  ./demographics/migrations/__pycache__ ./demographics/__pycache__ ./harvard/__pycache__
python manage.py migrate
python manage.py makemigrations demographics
python manage.py sqlmigrate demographics 0001
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
