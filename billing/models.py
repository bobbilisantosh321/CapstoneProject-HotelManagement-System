# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for billing with billing id as primary key..

class Billing(models.Model):
    billing_id = models.AutoField(primary_key=True)
    billing_date = models.CharField(max_length=255, default = "", unique=True)
    billing_booking_id = models.CharField(max_length=20, default = "")
    billing_room_rent = models.CharField(max_length=255, default = "")
    billing_food_bill = models.EmailField(max_length=255, default = "")
    billing_food_bill = models.EmailField(max_length=255, default = "")
    billing_description = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.billing_id