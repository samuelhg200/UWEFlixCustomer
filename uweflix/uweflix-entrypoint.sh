#!/bin/sh

echo "Waiting for Postgres Database Service to start..."

./wait-for db:5432

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000