from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """
    Unit Tests for Home App
    """

    def test_homepage(self):
        """ Test home page renders correct page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_context(self):
        """ Test if text is rendered properly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Nails Art!")
        self.assertContains(
            response, "It is not just nails art. It is an ART.")
