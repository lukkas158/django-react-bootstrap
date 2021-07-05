from django.http import response
from rest_framework.test import APITestCase
from users.models import User


class UserTesting(APITestCase):

    def post_user(self, data={}):

        user_data = {"name": "Lucas",  "email": "lucas@gmail.com",
                     "password": "123", "date_of_birth": "1996-03-19"}

        user_data.update(data)
        response = self.client.post("/api/users/", data=user_data)
        return response

    def test_registration(self):
        response = self.post_user()
        self.assertEqual(response.status_code, 201)

    def test_user_update_password(self):

        response = self.post_user()

        user = User.objects.all().first()
        old_password = user.password

        response = self.client.patch(
            f"/api/users/{user.id}/", data={"password": "1235"})
        self.assertEqual(response.status_code, 200)

        user = User.objects.all().first()
        new_password = user.password

        self.assertNotEqual(old_password, new_password)

    def test_login_sucess(self):

        self.post_user()

        response = self.client.post(
            "/api/token/", data={"email": "lucas@gmail.com", "password": "123"})

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json().get("access", None), None)
        self.assertNotEqual(response.json().get("refresh", None), None)
