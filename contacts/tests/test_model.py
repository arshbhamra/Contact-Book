from django.test import TestCase
from django.contrib.auth.models import User
from contacts.models import Contacts

class ContactModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username= "Josh",
            password= "123" 
        )

    def test_contact_is_saved(self):
        contact = Contacts.objects.create(
            user= self.user,
            name="Josh Friend",
            phone="1234",
            email="one@one.com",
            city="freeworld"
        )

        self.assertIsNotNone(contact.pk)

    def test_contact_belongs_to_user(self):
        contact = Contacts.objects.create(
            user=self.user,
            name="josh two",
            phone="12121"
        )
        
        self.assertEqual(contact.user, self.user)

    def test_contact_can_be_retrived(self):
        contact = Contacts.objects.create(
            user=self.user,
            name="third",
            phone="1212"
        )
        
        self.assertEqual(contact.name, "third")