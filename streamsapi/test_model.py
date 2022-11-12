from django.test import TestCase
from streamsapi.models import Matches
from django.test import TestCase
from django.contrib.auth.models import AbstractBaseUser,UserManager

class TestAppModels(TestCase):

    def test_model_str(self):
        title = Matches.objects.create(title="Model Testing")
        description = Matches.objects.create(description="desc")
        embed_code = Matches.objects.create(embed_code="url")
        self.assertEqual(str(title),"Model Testing")
