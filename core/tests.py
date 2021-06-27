from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Todo

class TodosApiTestCase(APITestCase):
    def create_todo(self):
        data = {
            'title': "New Todo", 
            'description': 'New Todo Description',
            'completed': True,
        }
        response = self.client.post(reverse('todo-create'), data)
        return response

    def authenticate_user(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password1': 'test-user-password1',
            'password2': 'test-user-password1',
        }
        self.client.post(reverse('register'), data)

        response = self.client.post(reverse('login'), {'email': 'testuser@gmail.com', 
                                                        'password': 'test-user-password1',})
        
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

class TestTodo(TodosApiTestCase):

    def test_should_not_create_without_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # TEST FOR CREATING TODO ITEM
    def test_should_create_todo(self):
        previous_todo_count = Todo.objects.all().count()
        self.authenticate_user()
        
        response = self.create_todo()
        # check if the data base updated after creating the todo
        self.assertEqual(Todo.objects.all().count(), previous_todo_count + 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Todo")
        self.assertEqual(response.data['description'], "New Todo Description")
        self.assertEqual(response.data['completed'], True)

    # TEST FOR RETRIEVING ALL TODO ITEMS
    def test_todo_lists(self):
        self.authenticate_user()
        response = self.client.get(reverse('todo-lists'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # CHECK THAT THE RESPONSE IS A LIST 
        self.assertIsInstance(response.data, list)
    
    # TEST FOR RETRIEVING ALL COMPLETED TODO ITEM
    def test_todo_completed_lists(self):
        self.authenticate_user()
        response = self.client.get(reverse('completed-todo'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # TEST FOR RETRIEVING ALL UNCOMPLETED TODO ITEM
    def test_todo_uncompleted_lists(self):
        self.authenticate_user()
        response = self.client.get(reverse('uncompleted-todo'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestTodoDetail(TodosApiTestCase):
    
    # TEST FOR RETRIEVING ONE TODO ITEM
    def test_retrieve_one_todo_item(self):
        self.authenticate_user()
        response = self.create_todo()
        todo_id = response.data['id']
        res = self.client.get(reverse('todo-details', kwargs={'pk':todo_id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=todo_id)
        self.assertEqual(todo.title, res.data['title'])
    
    # TEST FOR UPDATING A TODO ITEM
    def test_updates_a_todo_item(self):
        self.authenticate_user()
        res = self.create_todo()
        todo_id = res.data['id']

        response = self.client.put(reverse('todo-update', kwargs={'pk':todo_id}), {
            'title': 'Updated Title from Test',
            'description': 'Updated Description from Test',
            'completed': False
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # check if the item really updated
        updated_todo_item = Todo.objects.get(id=todo_id)
        self.assertEqual(updated_todo_item.completed, False)

        todo = Todo.objects.get(id=todo_id)
        self.assertEqual(response.data['title'], todo.title)

    # TEST FOR DELETING A TODO ITEM
    def test_deletes_a_todo_item(self):
        self.authenticate_user()
        res = self.create_todo()
        todo_id = res.data['id']
        previous_db_todo_count = Todo.objects.all().count()

        response = self.client.delete(reverse('todo-delete', kwargs={'pk':todo_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Todo.objects.all().count(), previous_db_todo_count - 1)