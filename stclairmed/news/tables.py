import django_tables2 as tables
from .models import Announcement


class AnnouncementTable(tables.Table):
    class Meta:
        model = Announcement
        fields = ('title', 'body', 'date', 'time')
        attrs = {'class':'table'}