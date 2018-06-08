import django_tables2 as tables
from .models import Newsletter


class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        fields = ('month', 'year')
        attrs = {'class':'table'}