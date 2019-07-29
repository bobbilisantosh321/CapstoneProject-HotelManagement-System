# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for food with food id as primary key..


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_booking_id = models.CharField(max_length=255, default = "", unique=True)
    food_amount = models.CharField(max_length=20, default = "")
    food_date = models.CharField(max_length=255, default = "")
    food_description = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.food_id