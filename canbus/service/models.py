from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class Trips(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    start_fuel = models.CharField(max_length=50)
    end_fuel = models.CharField(max_length=50)

    def get_total_gas(self):
        return self.end_gas_level - self.start_gas_level

    def get_total_miles(self):
        return self.end_miles - self.start_miles

    def get_total_time(self):
        return self.end_time - self.start_time

    def __str__(self):
        return self.name


class TripInformation(models.Model):
    trip = models.ForeignKey(Trips)
    time = models.DateTimeField(auto_now_add=False)
    rpm = models.CharField(max_length=100)
    mph = models.CharField(max_length=100)
    throttle = models.CharField(max_length=100)
    load = models.CharField(max_length=100)
    fuel_status = models.CharField(max_length=100)

    def __str__(self):
        return self.id
