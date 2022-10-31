from django.contrib import admin

# Register your models here.

from .models import Irrigation, Measurement, Plant, Pot

admin.site.register(Plant)
admin.site.register(Pot)
admin.site.register(Measurement)
admin.site.register(Irrigation)