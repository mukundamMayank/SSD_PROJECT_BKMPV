python3 -m venv venv
source venv/bin/activate
pip install django
pip3 install djangorestframework
django-admin startproject djangoproject .
python manage.py runserver
python manage.py startapp home
python manage.py startapp participant
python3 manage.py makemigrations

#To activate venv and run app
python3 -m venv venv
source venv/bin/activate
python manage.py runserver
