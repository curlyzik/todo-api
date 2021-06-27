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
/todo/create/ # for creating new todo
/todo # for listing all todos created by the author/user
/todo/completed/ # for listing all the completed todos of the author/user
/todo/uncompleted/ # for listing all the uncompleted todos of the author/user
/todo/details/<todo_id>/ # for getting the details of a todo
/todo/update/<todo_id>/ # for updating a todo
/todo/delete/<todo_id>/ # for deleting a todo
```
The Todo Api and User Api can be found in the [core/api folder](https://github.com/curlyzik/todo-api/tree/main/core/api) and [users/api folder](https://github.com/curlyzik/todo-api/tree/main/users/api) respectively

## Integration of Unit Testing For Each EndPoint
The Todo Unit Test and User Unit Test can be found in the [core folder](https://github.com/curlyzik/todo-api/blob/main/core/tests.py) and [users folder](https://github.com/curlyzik/todo-api/blob/main/users/tests.py) respectively

## Test Endpoints With POSTMAN
You can test each endpoints using POSTMAN with the the [POSTMAN JSON File](https://github.com/curlyzik/todo-api/blob/main/Todo.postman_collection.json)

Steps:
1. Download PostMan
2. Download the [JSON FILE](https://github.com/curlyzik/todo-api/blob/main/Todo.postman_collection.json)
3. Open PostMan, Click on Collection.
4. Click on Import and upload the download file
