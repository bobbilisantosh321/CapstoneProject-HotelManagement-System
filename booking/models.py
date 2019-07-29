# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for booking with booking room id as primary key.

class Booking(models.Model):
    booking_room_id = models.AutoField(primary_key=True)
    booking_customer_id = models.CharField(max_length=255, default = "", unique=True)
    booking_from_date = models.CharField(max_length=20, default = "")
    booking_to_date = models.CharField(max_length=255, default = "")
    booking_status = models.EmailField(max_length=255, default = "")
    booking_amount = models.EmailField(max_length=255, default = "")
    billing_description = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.booking_room_id