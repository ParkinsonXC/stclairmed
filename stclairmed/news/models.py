from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    body = models.TextField(max_length=4000, blank=False)
    date = models.DateField(auto_now_add=True, blank=False)
    time = models.TimeField(auto_now=True, blank=False)
    img = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title + ' ' + str(self.date)

