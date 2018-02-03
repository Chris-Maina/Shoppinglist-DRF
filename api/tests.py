""" api/tests.py """
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Shoppinglist, User

# Create your tests here.
class ModelTestCases(TestCase):
    """ Test cases for models """
    def setUp(self):
        """ Define test variables """
        self.shoppinglist = Shoppinglist(
            name="Christmass shopping", description="Shopping for 2018 christmass")
        self.test_user = User(username="test", email="test@gmail.com", password="testpassword")

    def test_shoppinglist_model(self):
        """ Test Shoppinglist model is created """
        old_count = Shoppinglist.objects.count()
        self.shoppinglist.save()
        new_count = Shoppinglist.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_user_model(self):
        """ Test User model """
        old_count = User.objects.count()
        self.test_user.save()
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)
class ViewTestCases(TestCase):
    """ Test cases for views """
    def setUp(self):
        """ Define test client """
        self.client = APIClient()
        self.shoppinglist_data = {
            "name": "Easter shopping", "description": " Shopping to gift mum this easter."}
        self.response = self.client.post(
            reverse('api:create_list'),
            self.shoppinglist_data,
            format="json")
        # get shoppinglist from model
        self.shoppinglist = Shoppinglist.objects.get()

    def test_shoppinglist_is_created(self):
        """ test api can create a shoppinglist  """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_single_shoppinglist(self):
        """ test api can get one shoppinglist """
        response = self.client.get(
            reverse('api:shoppinglist_details', kwargs={'pk': self.shoppinglist.id}),
            format="json")
        self.assertContains(response, self.shoppinglist)

    def test_api_can_edit_shoppinglist(self):
        """ test api can get edit a shoppinglist """
        new_shoppinglist_data = {
            "name": "Christmass shopping", "description": " Christmass gift 2018."}
        response = self.client.put(
            reverse('api:shoppinglist_details', kwargs={'pk': self.shoppinglist.id}),
            new_shoppinglist_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_shoppinglist(self):
        """ test api can get delete a shoppinglist """
        response = self.client.delete(
            reverse('api:shoppinglist_details', kwargs={'pk': self.shoppinglist.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
