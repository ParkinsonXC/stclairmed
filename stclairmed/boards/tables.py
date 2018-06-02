import django_tables2 as tables
from .models import Specialty, Practice, Doctor

class PracticeTable(tables.Table):
    class Meta:
        model = Practice

        
