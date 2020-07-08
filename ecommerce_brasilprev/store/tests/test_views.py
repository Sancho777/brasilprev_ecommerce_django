# conding=utf-8

from django.test import TestCase, Client


class HomeViewTestCase(TestCase):

    def test_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.status_code, 200)
