import django_tables2 as tables
from .models import Specialty, Practice, Doctor

class PracticeTable(tables.Table):
    class Meta:
        model = Practice
        fields = ('name', 'address', 'city', 'state', 'phone_number')

# TODO: Make this an anchor tag search instead?
class SpecialtyTable(tables.Table):
    class Meta:
        model = Specialty
        fields = ('name',)

class DoctorTable(tables.Table):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'title', 'practice', )