from django.test import TestCase


# This allows us to refer to an endpoint by its name instead of its path.
from django.urls import reverse


class RssIndexViewTests(TestCase):
    # This test uses the client object supplied by the TestCase class to “mock” an HTTP request to the index view.
    def test_no_feed(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["feed"], None)


def test_user_feed(self):
    response = self.client.get(reverse("index") + "http://www.nba.com/rss/nba_rss.xml")

    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(response.context["feed"], None)