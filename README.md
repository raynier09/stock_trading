# Simple Stock Trading

Simple Stock trading built with Django REST framework

Add cors_header, rest_framework module
Additional JWT token authentication

To get started: 

switch to revised branch.

create an account and use this command:
python manage.py createsuperuser

migrate stocks app:
python manage.py makemigrations stocks
python manage.py migrate
then run the Django server

To view the API Endpoint. login to Django Administration before go to the API endpoint.

View the revise branch to check the completed task.


JWT Web Token
    - http://127.0.0.1:8000/token-auth/

Place order of stocks
    - http://127.0.0.1:8000/api/stocks/

View ordered stocks and summation
    - http://127.0.0.1:8000/api/stocks/
