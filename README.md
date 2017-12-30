# Recipebot
A chatbot that lets you retrieve interesting recipes. 

## Prerequisites
You need Python 3.x for this project to work properly. Also, make sure you use a virtual environment 
to isolate this project from other work you're doing on your computer.

## Quickstart
Execute the following steps to get started:

* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py createsuperuser`

When this is done, execute the following command to run the application:

* `python manage.py runserver`

## Getting around in the application
The current version is limited to a REST api and admin interface. You can access these through the following URLs:

* [http://localhost:8000/admin](http://localhost:8000/admin) Administration interface
* [http://localhost:8000/docs](http://localhost:8000/docs) Documentation

You can login using the super user you created earlier.
