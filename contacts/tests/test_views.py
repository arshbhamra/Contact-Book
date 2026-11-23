from django.contrib.auth.models import User
from contacts.models import Contacts
from django.test import TestCase 
from django.urls import reverse


class ContactViewTest(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create_user(
            username="user1",
            password="pass1"
        )
        
        self.other_user = User.objects.create_user(
            username="user2",
            password="pass2"
        )
        
        self.contact = Contacts.objects.create(
            user = self.user,
            name = "oneF",
            phone = "121"
        )
        
        self.other_contact = Contacts.objects.create(
            user = self.other_user,
            name = "twoF",
            phone = "4432"
        )
        
    def test_page_req_login(self):
        response = self.client.get("/app/contacts/")
        
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)
        
        
    def test_logged_user_can_view_contacts(self):
        self.client.force_login(self.user)
        
        response = self.client.get("/app/contacts/")

        # self.assertTrue(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "oneF")



    def test_recent_page_require_login(self):
        response = self.client.get("/app/recent/")

        self.assertEqual(response.status_code, 302)
        self.assertIn("app/login/", response.url)



    def test_user_can_view_own_contact(self):
        self.client.force_login(self.user)
        
        # response = self.client.get(
        #     f"/app/contact/{self.contact.pk}/"
        # )
        
        response = self.client.get(
            reverse("contact_detail", args=[self.contact.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "oneF")
        
        
    def test_other_user_cannot_see_user_contact(self):
        self.client.force_login(self.user)
        
        # response = self.client.get("/app/contacts")
        response = self.client.get(reverse("contacts"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "oneF")
        self.assertNotContains(response, "twoF")
        
        
        