import json

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from api.models import Stats


# Create your tests here.

# It tests the smallest function, the stats function, and the stats model
class TestSmallestCase(APITestCase):

    def test_smalltest(self):
        """
        The function takes a list of numbers and returns the smallest number in the list
        """
        url = reverse('smallest')
        data = {"array":[1]}
        response = self.client.get(url, data, format=json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_smalltest_error(self):
        """
        It tests the smallest function in the views.py file. It tests the error case where the array
        contains a string.
        """
        url = reverse('smallest')
        data = {"array":[1, "asdasdas"]}
        response = self.client.get(url, data, format=json)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_stats(self):
        """
        The function tests the stats endpoint with a bad request
        """
        url = reverse('stats')
        data = {"stats":[1]}
        response = self.client.get(url, data, format=json)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_stats_create(self):
        """
        We create a Stats object with a result of 40 and a total of 100, and then we assert that the stats
        object is an instance of Stats, that the result is 40, and that the total is 100
        """
        stats = Stats.objects.create(
            result=40,
            total=100
        )
        self.assertIsInstance(stats, Stats)
        self.assertEqual(stats.result, 40)
        self.assertEqual(stats.total, 100)

    def test_stats_query(self):
        """
        We create a Stats object, then we query the database to see if the object was created
        """
        stats = Stats.objects.create(
            result=40,
            total=100
        )
        queryResult = Stats.objects.filter(result=stats.result).count()
        queryTotal = Stats.objects.all().count()
        self.assertEqual(queryResult, 1)
        self.assertEqual(queryTotal, 1)

