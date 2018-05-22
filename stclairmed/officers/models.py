from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=75, default='', blank=True)

    def __str__(self):
        return self.name

class Officer(models.Model):
    first_name = models.CharField(max_length=30, default='')
    middle_init = models.CharField(max_length=1, default='', blank=True)
    last_name = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=10, default='', blank=True)
    position = models.CharField(max_length=40, default='', blank=True)
    role = models.ForeignKey(Role, related_name='officers', on_delete='PROTECT')

    def __str__(self):
        return '{0} {1}, {2}'.format(self.first_name, self.last_name, self.title)


