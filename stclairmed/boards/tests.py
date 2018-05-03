from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, directory

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)



class DirectoryTests(TestCase):
    def test_directory_view_status_code(self):
        url = reverse('directory')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_directory_url_resolves_directory_view(self):
        view = resolve('/directory/')
        self.assertEquals(view.func, directory)
