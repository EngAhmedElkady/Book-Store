import email
from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CusomUserTest(TestCase):

    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username="ahmed",
            email="ahmed@gmail.com",
            password="as112233"
        )

        self.assertEqual(user.username,"ahmed")
        self.assertEqual(user.email,"ahmed@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        user=User.objects.create_superuser(
            username="ahmed",
            email="ahmed@gmail.com",
            password="as112233"
        )

        self.assertEqual(user.username,"ahmed")
        self.assertEqual(user.email,"ahmed@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

