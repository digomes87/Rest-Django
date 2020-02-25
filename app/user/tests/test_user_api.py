from django.test import  TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import  APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Teste je user api public"""
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creatinf user with valid payload is success"""
        payload = {'email': 'teste@gmail.com', 'password': 'teste12312','name': 'Teste name'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """test creatinf user that already exist"""
        payload = {'email': 'test@gmail.com', 'password': 'test123'}
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """password is too short"""
        payload = {'email': 'test@gmail.com', 'password': 'tes'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """create a toke for user"""
        payload = {'email': 'teste@gmail.com', 'password': 'teste123'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """test that token is not created"""
        create_user(email='teste@gmail.com', password='test123')
        payload = {'email': 'teste@gmail.com', 'password': 'wrong'}

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_created_token_no_user(self):
        """test that token is not created if user doesn"""
        payload = {'email': 'teste@gmail.com', 'password': 'test123'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """test that email and pass are required"""
        res = self.client.post(TOKEN_URL, {'email': 'one',
                                           'password': '123test'})
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
