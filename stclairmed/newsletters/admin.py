from django.contrib import admin
from .models import Newsletter, Subscriber

# Register your models here.


admin.site.register(Newsletter)
admin.site.register(Subscriber)