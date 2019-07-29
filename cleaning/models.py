# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for cleaning with cleaning id as primary key.

class Cleaning(models.Model):
    cleaning_id = models.AutoField(primary_key=True)
    cleaning_date = models.CharField(max_length=255, default = "", unique=True)
    cleaning_room_id = models.CharField(max_length=255, default = "")
    cleaning_description = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.cleaning_id