# PantryPal - An AI Fueled Recipe Generator


# Release Notes

- Version 1.0:
- - New Features:
- - - Implementation of being able to add food items into user's pantry, generating a recipe from GPT that uses the ingredients in the user's pantry, able to search and find other users to be friends so you can see their recipe posts as well.


- - Bug Fixes:
- - - Made it so if the user is not logged in and tries to access the feed page it redirects them to the login page first to avoid null pointers from the non-signed in user.
- - - Made it so the format of the GPT response makes sense for the goal of the website


- - Known Bugs and Defects:
- - - There is no page for the original host page only which means the user has to type in a url extension to see the website


# Install Guide

- Pre-requisites: 
- - Create a file and folder in Project2/pantrypal/keys/keys.py with a variable called OPEN_AI_VAR set to your Open AI API key string
- - Need python 3.11.4 or newer installed


- Dependencies and Libraries
- - Need to pip install Django
- - Need to pip install Open AI
- - Need to pip install Pillow


- Download & Build Instructions
- - You can download the project off of github by cloning the code by running the command: 
- - git clone https://github.com/CS3300Group13/Project2.git


- Application Installation & Run
- - Need to run these command line prompts in the Project2/pantrypal/ folder
- - python manage.py makemigrations
- - python manage.py migrate --run-syncdb
- - python manage.py runserver
- - Then you can access the server at your local host


- Troubleshooting
- - Common errors during installation involve not creating the superuser for Django which can be done using the command: python manage.py createsuperuser
- - You also need to add a PantryPal user to the superuser's account because they have different features
