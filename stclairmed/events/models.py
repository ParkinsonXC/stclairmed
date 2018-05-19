from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    date_of = models.DateField()
    time_of = models.TimeField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title