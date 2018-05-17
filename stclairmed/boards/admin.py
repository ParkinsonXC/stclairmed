from django.contrib import admin
from .models import Specialty, Practice, Doctor
# Register your models here.
admin.site.register(Specialty)
admin.site.register(Practice)
admin.site.register(Doctor)