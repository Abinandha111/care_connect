from django.db import models

# Create your models here.


class Doctor(models.Model):

    name = models.CharField(max_length=200)

    specialization = models.CharField(max_length=200)

    contact = models.CharField(max_length=15)

    email = models.CharField(max_length=100)

    experience = models.IntegerField()

    fee = models.DecimalField(max_digits=10,decimal_places=2)