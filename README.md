# PantryPal - An AI Fueled Recipe Generator


# Release Notes

- Version 1.0:
- - New Features:
- - Bug Fixes:


# Install Guide

- Pre-requisites: 
- - Create a folder called keys that has keys.py file with a variable called OPEN_AI_VAR set to your Open AI API key
- - Need python 3.11.4 or newer installed


- Dependencies and Libraries
- - Need to pip install Django
- - Need to pip install Open AI


- Download & Build Instructions
- - You can download the project off of github by cloning the code by running the command: 
- - git clone https://github.com/CS3300Group13/Project2.git


- Application Installation & Run
- - Need to run these command line prompts in the Project2/pantrypal/ folder
- - python manage.py makemigrations
- - python manage.py migrate
- - python manage.py runserver
- - Then you can access the server at your local host


- Troubleshooting
- - Common errors during installation involve not creating the superuser for Django which can be done using the command: python manage.py createsuperuser
- - You also need to add a PantryPal user to the superuser's account because they have different features