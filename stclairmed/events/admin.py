from django.contrib import admin
from .models import Event, Location, RSVP
from events.forms import EventForm

class EventAdmin(admin.ModelAdmin):
    form = EventForm
    fieldsets =[
        (None, {'fields': ['title', 'description', 'location']}),
        ('Date Information', {'fields': ['date_of', 'time_of']})
    ]



admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(RSVP)

