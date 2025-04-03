#!/usr/bin/env bash

# 1. Installer les dépendances Python
pip install -r requirements.txt

# 2. Ensuite, lancer collectstatic
python manage.py collectstatic --noinput
