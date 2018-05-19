from django.contrib import admin
from .models import Event
from events.forms import EventForm

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    fieldsets =[
        (None, {'fields': ['title', 'description']}),
        ('Date Information', {'fields': ['date_of', 'time_of']})
    ]



admin.site.register(Event, EventAdmin)

