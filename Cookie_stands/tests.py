from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Cookie_stand
from django.contrib.auth import get_user_model


class Cookie_standAPITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save()
        # Create some test data for Cookie_stand
        cookie_stand=Cookie_stand.objects.create(
            location="Test Location 1",
            minimum_customers_per_hour=10,
            maximum_customers_per_hour=50,
            average_cookies_per_sale=2.5,
        )
        cookie_stand.save
        cookie_stand2= Cookie_stand.objects.create(
            location="Test Location 2",
            minimum_customers_per_hour=20,
            maximum_customers_per_hour=60,
            average_cookies_per_sale=3.0,
        )
        cookie_stand2.save

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")


    def test_cookie_stand(self):
        cookie_stand = Cookie_stand.objects.get(id=1)
        location = str(cookie_stand.location)
        minimum_customers_per_hour = str(cookie_stand.minimum_customers_per_hour)
        maximum_customers_per_hour = str(cookie_stand.maximum_customers_per_hour)
        average_cookies_per_sale = str(cookie_stand.average_cookies_per_sale)

        self.assertEqual(location, "Test Location 1")
        self.assertEqual(minimum_customers_per_hour, "10")
        self.assertEqual(
            maximum_customers_per_hour, "50"
        )
        self.assertEqual(average_cookies_per_sale, "2.5")

    def test_get_cookie_stand(self):
        url = reverse("Cookie_stand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Cookie_stand_list = response.data
        self.assertEqual(len(Cookie_stand_list), 1)
        self.assertEqual(Cookie_stand_list[0]["location"], "Test Location 1")





