from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class ItemTest(TestCase):
    def test_create_item(self):
        item = Item.objects.create(
            name='Test Item',
            description='This is a test item',
            category='Test Category',
            amount=10,
        )
        retrieved_item = Item.objects.get(name='Test Item')

        self.assertEqual(item, retrieved_item)

