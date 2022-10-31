from django.db import models

# Create your models here.

class Plant(models.Model): # stores data about each plant that can be placed in a pot
    plant_name = models.CharField(max_length=50, primary_key=True, null=False)
    start_pct  = models.IntegerField(default=45)
    stop_pct   = models.IntegerField(default=55)
    def __str__(self):
         return self.plant_name

class Pot(models.Model): # stores data about each pot in the product
    pot_id              = models.IntegerField(default=-1, primary_key=True, null=False) # placeholder to be replaced in the frontend
    plant_name          = models.CharField(default='Empty', max_length=50)
    irrigation_last     = models.DateTimeField(null=True)
    irrigation_duration = models.IntegerField(default=-1)                               # placeholder to be replaced in the frontend
    irrigation_amount   = models.IntegerField(default=-1)                               # placeholder to be replaced in the frontend
    measurement_last    = models.DateTimeField(null=True)
    moisture_value      = models.IntegerField(default=-1)                              # placeholder to be replaced in the frontend
    temperature_value   = models.IntegerField(default=-363)                             # placeholder to be replaced in the frontend
    def __int__(self):
        return self.pot_id

class Measurement(models.Model): # stores data about each measurement done by the microcontroller
    pot_id            = models.IntegerField(default=-1, null=False)                   # placeholder to be replaced in the frontend
    measurement_time  = models.DateTimeField(null=False)
    moisture_value    = models.IntegerField()                                         # placeholder to be replaced in the frontend
    temperature_value = models.IntegerField()                                         # placeholder to be replaced in the frontend
    models.UniqueConstraint(name='unique_measurement', fields=['pot_id', 'measurement_time'])
    def __str__(self):
        return '%d, %s' %(self.pot_id, self.measurement_time)

class Irrigation(models.Model): # stores data about each irrigation done by the microcontroller
    pot_id              = models.IntegerField(default=-1, null=False)         # placeholder to be replaced in the frontend
    irrigation_time     = models.DateTimeField(null=False)
    irrigation_value    = models.IntegerField()                               # placeholder to be replaced in the frontend
    irrigation_duration = models.IntegerField()                               # placeholder to be replaced in the frontend
    models.UniqueConstraint(name='unique_irrigation', fields=['pot_id', 'irrigation_time'])
    def __str__(self):
        return '%d, %s' %(self.pot_id, self.irrigation_time)