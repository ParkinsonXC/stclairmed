import django_tables2 as tables
from .models import Officer, Role

class OfficerTable(tables.Table):
    class Meta:
        model = Officer
        fields = ('first_name', 'middle_init', 'last_name')
        attrs = {'class':'table'}