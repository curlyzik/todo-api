from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthenticationApiTestCase(APITestCase):

    def register_user(self):
        data = {
            'username': 'new-user',
            'email': 'new-user@gmail.com',
            'password1': 'new-password',
            'password2': 'new-password'
        }
        response = self.client.post(reverse('register'), data)
        return response

class TestUserAuthentication(UserAuthenticationApiTestCase):
    
    # TEST FOR USER REGISTRATION
    def test_user_registration(self):
        previous_db_count_of_users = User.objects.all().count()
        
        response = self.register_user()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # CHECK TO CONFIRM IF THE USER IS SUCCESSFULLY RESGISTERED IN THE DB
        current_db_count_of_users = User.objects.all().count()
        self.assertEqual(current_db_count_of_users, previous_db_count_of_users + 1)

    # TEST FOR USER LOGIN
    def test_user_login(self):
        self.register_user()

        response = self.client.post(reverse('login'), {'email': 'new-user@gmail.com',
                                                        'password': 'new-password',})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)