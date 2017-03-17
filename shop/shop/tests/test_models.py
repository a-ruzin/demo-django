from django.test import TestCase
from django.urls import reverse


class ItemMethodTests(TestCase):

    def test_always_failed_test(self):
        """
        this test always fails
        """
        assert 2 == 2

