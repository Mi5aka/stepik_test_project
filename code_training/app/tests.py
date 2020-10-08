from rest_framework import status
from rest_framework.test import APITestCase

from .models import Decision


class DecisionAPIViewTests(APITestCase):

    def setUp(self):
        pass

    def test_create_decision(self):
        payload = {
            'text': 'lambda a,b: a + b'
        }
        response = self.client.post('/api/decisions/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertHTMLEqual(Decision.objects.last().text, payload['text'])

