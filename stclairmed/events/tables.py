import django_tables2 as tables
from .models import Event


class EventTable(tables.Table):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date_of', 'date_posted')
        attrs = {'class':'table'}