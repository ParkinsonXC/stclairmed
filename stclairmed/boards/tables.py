import django_tables2 as tables
from .models import Specialty, Practice, Doctor
from events.models import Event

class PracticeTable(tables.Table):
    class Meta:
        model = Practice
        fields = ('name', 'address', 'city', 'state', 'phone_number')
        attrs = {'class':'table'}


class SpecialtyTable(tables.Table):
    class Meta:
        model = Specialty
        fields = ('name',)
        attrs = {'class':'table'}
        

class DoctorTable(tables.Table):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'title', 'practice', )
        attrs = {'class':'table'}
        