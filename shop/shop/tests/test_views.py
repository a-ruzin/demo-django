from django.test import TestCase
from django.urls import reverse


class ItemMethodTests(TestCase):

    def test_2(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
