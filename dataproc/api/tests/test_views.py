# Python imports
import json

# Django imports
from django.test import TestCase, Client
from django.urls import reverse

# Models imports

class TestViews(TestCase):

	def test_sotreInput(self):
		client = Client()
		response = client.get(reverse('store_input'))
		self.assertEquals(response.status_code, 200)
