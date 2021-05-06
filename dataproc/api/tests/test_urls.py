# Django imports
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Views Imports
from api.views.input_view import storeInput

class TestUrls(SimpleTestCase):

	def test_add_input_url_resolves(self):
		url = reverse('store_input')
		self.assertEquals(resolve(url).func, storeInput)