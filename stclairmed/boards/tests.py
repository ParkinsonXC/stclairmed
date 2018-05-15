from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, directory, contact

# Create your tests here.
class HomeTests(TestCase):

    def setUp(self):
        url=reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_navigation_links(self):
        directory_url = reverse('directory')
        contact_url = reverse('contact')
        officers_url = reverse('officers')
        events_url = reverse('events')
        news_url = reverse('news')
        hospitals_url = reverse('hospitals')
        links_url = reverse('links')
        contact_url = reverse('contact')

        self.assertContains(self.response, f'href="{directory_url}"')
        self.assertContains(self.response, f'href="{contact_url}"')
        self.assertContains(self.response, f'href="{officers_url}"')
        self.assertContains(self.response, f'href="{events_url}"')
        self.assertContains(self.response, f'href="{news_url}"')
        self.assertContains(self.response, f'href="{hospitals_url}"')
        self.assertContains(self.response, f'href="{links_url}"')
        self.assertContains(self.response, f'href="{contact_url}"')

class DirectoryTests(TestCase):

    def test_directory_view_status_code(self):
        url = reverse('directory')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_directory_url_resolves_directory_view(self):
        view = resolve('/directory/')
        self.assertEquals(view.func, directory)

class ContactTests(TestCase):

    def test_contact_view_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_contact_url_resolves_contact_view(self):
        view = resolve('/contact/')
        self.assertEquals(view.func, contact)

class HospitalTests(TestCase):

    def test_hospital_view_status_code(self):
        url = reverse('hospitals')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)