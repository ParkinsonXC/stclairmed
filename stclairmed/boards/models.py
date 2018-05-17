from django.db import models

# Create your models here.
class Specialty(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#This is a comment in order to activate the branch

class Practice(models.Model):
    name = models.CharField(max_length=45, unique=True)
    address = models.CharField(max_length = 50, unique=True)
    city = models.CharField(max_length=25, default='')
    state = models.CharField(max_length=25, default='IL')
    zip_code = models.CharField(max_length=5, default='')
    phone_number = models.CharField(max_length=11, default='')
    website = models.CharField(max_length=50, default='')

    def __str__(self):
        return '{0} {1}, {2} {3}'.format(self.address, self.city, self.state, self.zip_code)


class Doctor(models.Model):
    first_name = models.CharField(max_length=25)
    middle_init = models.CharField(max_length=1)
    last_name = models.CharField(max_length=25)
    title = models.CharField(max_length=10)
    practice = models.ForeignKey(Practice, related_name='doctors', on_delete='CASCADE')
    specialty = models.ForeignKey(Specialty, related_name='doctors', on_delete='CASCADE')

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)