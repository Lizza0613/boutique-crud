#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# ¡Estas dos líneas juntas crean las tablas que faltan!
python manage.py makemigrations
python manage.py migrate