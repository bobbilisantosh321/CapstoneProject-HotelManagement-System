# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for laundry with laundry id as primary key..

class Laundry(models.Model):
    laundry_id = models.AutoField(primary_key=True)
    laundry_booking_id = models.CharField(max_length=255, default = "", unique=True)
    laundry_amount = models.CharField(max_length=20, default = "")
    laundry_date = models.CharField(max_length=255, default = "")
    laundry_description = models.EmailField(max_length=255, default = "")
    def __str__(self):
        return self.laundry_id