from rest_framework.test import APITestCase,APIClient
from django.urls import reverse


class TestSetup(APITestCase):

    def setUp(self):
        self.matches_url=reverse('matches')

        self.user_data={
            'title':"title",
            'description':"description",
            'embed_code':"embed_code",
        }
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
