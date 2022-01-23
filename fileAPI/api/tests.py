from django.test import TestCase


class TestFileApi(TestCase):
    def test_get_file(self):
        response = self.client.get('/file/')
        print(response.json())
