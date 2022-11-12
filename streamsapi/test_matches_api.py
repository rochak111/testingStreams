from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import ListMatches
from rest_framework.test import APITestCase

class ApiUrlsTests(SimpleTestCase):

    def test_get_matches_is_resolved(self):
        url = reverse('matches')
        self.assertEquals(resolve(url).func.view_class,ListMatches)

