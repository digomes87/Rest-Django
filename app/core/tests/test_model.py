from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email(self):
        """ Test for create user with email """

        email = 'teste@gmail.com'
        password = "qeqweei932"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """ New email """

        email = "testenew@email.com"
        user = get_user_model().objects.create_user(email,'teste123')
        self.assertEqual(user.email, email.lower())

    def test_email_invalid(self):
        """ Teste for new email invalid """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """teste for create new super user"""

        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)