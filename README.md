# Quinn AI - API
This is a Django Rest Framework app that provides an API for the mail browser extension Quinn AI. It connects to OpenAI's API to offer different AI services.

## Prerequisites
Before installing this app, make sure you have installed all necessary libraries. You can find them in the requirements.txt file.
##Installation
Clone the repository to your local machine.
Create a virtual environment and activate it.
Install the required packages by running pip install -r requirements.txt.
Run the database migrations by running python manage.py migrate.

## Models

## Branches
This project has three branches:

- dev: This branch is used for development and testing. Data is stored with an SQLite database.
- stage: This branch is hosted on Heroku, and is used for staging. Data is currently stored with an SQLite database.
- prod: This branch is used for production and should only contain stable code. Data should be stored with a PostgreSQL database. 
##Usage
To run the app, switch to the dev branch and run the command python manage.py runserver. The app will be available at http://127.0.0.1:8000.

The app provides the following end-points: 
- /api/email/
- /admin/email/
To access the admin back-office, you'll need to provide credentials for superuser account. To obtain so, you can create a superuser by running python manage.py createsuperuser.
Once it is done, you will have access to every dataset, with the ability to see, change and delete data. 

## Deploy
The stage branch is connected to the Heroku app. To deploy any change, you just have to push it on the stage branch, Heroku will automatically publish those changes within a minute.
