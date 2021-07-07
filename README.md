# TODO APP API

This is a todo app api built with Django and Django Rest Framework.
This app uses [dj_rest_auth](https://dj-rest-auth.readthedocs.io/en/latest/) and [simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for User Authentication

## API Endpoints

These are the api endpoints for the todo app

```bash
base url 
http://127.0.0.1:8000

# USER ENDPOINTS
/users/login/ # for logging in a user
/users/register/ # for registering a new user

# TODO ENDPOINTS
/todo/<user_id>/create/             #to create new todo
/todo/<user_id>/                    #to get all todos created by user
/todo/<user_id>/<todo_id>/          #to get todo details
/todo/<user_id>/<todo_id>/update/   #to update todo
/todo/<user_id>/<todo_id>/delete/   #to delete todo
/todo/<user_id>/completed/          #to get all completed todo by user
/todo/user_id>/uncompleted/         #to get all uncompleted todo  by user

```
The Todo Api and User Api can be found in the [core/api folder](https://github.com/curlyzik/todo-api/tree/main/core/api) and [users/api folder](https://github.com/curlyzik/todo-api/tree/main/users/api) respectively

## Integration of Unit Testing For Each EndPoint
The Todo Unit Test and User Unit Test can be found in the [core folder](https://github.com/curlyzik/todo-api/blob/main/core/tests.py) and [users folder](https://github.com/curlyzik/todo-api/blob/main/users/tests.py) respectively

## RUN APPLICATION WITH DOCKER
You can run this application if you have docker installed using these commands:
docker build --tag todo-api .
docker run --publish 8000:8000 todo-api
