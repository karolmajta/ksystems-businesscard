from django.test import TestCase
from django.test.client import Client

from django.contrib.auth.models import User

from ..models import BCardSite, BCardPage

class UrlsForSiteGetGeneratedTest(TestCase):
    
    def setUp(self):
        self.client = Client()