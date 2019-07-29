# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for room with room id as primary key..

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=255, default = "", unique=True)
    room_cost = models.CharField(max_length=20, default = "")
    room_type = models.CharField(max_length=255, default = "")
    room_description = models.EmailField(max_length=255, default = "")
    def __str__(self):
        return self.room_id