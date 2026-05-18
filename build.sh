#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Esto obliga a Django a rehacer los planos y meterlos a la fuerza
python manage.py makemigrations --merge --noinput
python manage.py makemigrations inventario --noinput
python manage.py migrate --noinput