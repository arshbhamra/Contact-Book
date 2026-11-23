from contacts.forms import ContactForm
from django.test import TestCase

class ContactFormTest(TestCase):
    
    def test_form_valid(self):
        form = ContactForm(data={
            "name":"arsh",
            "email":"one@one.com",
            "phone":"1212",
            "city":"mohali",
        })
        
        self.assertTrue(form.is_valid())
        
    def test_missing_req_name(self):
        form = ContactForm(data={
            "name":"",
            "city":"khanna",
            "phone":"1212",
            "email":"one@one.com"
        })
        
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        