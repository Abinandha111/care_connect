from django.db import models

# Create your models here.

class Appointment(models.Model):

    name = models.CharField(max_length=200)

    phone = models.CharField(max_length=15)

    doctor = models.PositiveIntegerField()

    appointment_date = models.DateField()

    appointment_time = models.TimeField(null=True)

    token = models.IntegerField(null=True)