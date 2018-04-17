from django.db import models

# Create your models here.
class Specialty(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Practice(models.Model):
    name = models.CharField(max_length=45, unique=True)
    address = models.CharField(max_length = 50, unique=True)
    number = models.IntegerField()
    specialty = models.ForeignKey(Specialty, related_name='practices', on_delete='CASCADE')