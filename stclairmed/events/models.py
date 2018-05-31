from django.db import models
from django.core.validators import MaxValueValidator

class Location(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        if len(self.name) > 0:
            return self.name + ' -- ' + self.address
        return self.address

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    location = models.ForeignKey(Location, related_name='events', on_delete='CASCADE')
    attendees = models.PositiveIntegerField(
        default=0, 
        validators=[MaxValueValidator(20)]
        )
    date_of = models.DateField()
    time_of = models.TimeField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class RSVP(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    guests = models.IntegerField(default=0, null=False)
    email = models.EmailField(blank=True, default='', unique=False, null=False)
    event = models.ForeignKey(Event, related_name='RSVPs', on_delete='CASCADE', null=False)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)