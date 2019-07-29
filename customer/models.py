# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# The model data for customer with customer id as primary key..

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_password = models.CharField(max_length=20, default = "")
    customer_level = models.CharField(max_length=255, default = '2')
    customer_sal = models.CharField(max_length=20, default = "")
    customer_first_name = models.CharField(max_length=255, default = "")    
    customer_middle_name = models.CharField(max_length=255, default = "")
    customer_last_name = models.CharField(max_length=255, default = "")	
    customer_gender = models.CharField(max_length=10, default = "")
    customer_address = models.TextField(default = "")
    customer_village = models.CharField(max_length=255, default = "")
    customer_state = models.CharField(max_length=255, default = "")
    customer_country = models.CharField(max_length=255, default = "")
    customer_landline = models.CharField(max_length=255, default = "")
    customer_mobile = models.CharField(max_length=255, default = "")
    customer_email = models.EmailField(max_length=255, default = "")
    customer_status = models.CharField(max_length=255, default = "")
    customer_deparment = models.CharField(max_length=255, default = "")
    customer_dob = models.CharField(max_length=255, default = "")
    customer_nationalty = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.customer_id

class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.state_name

class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.city_name

class country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=255, default = "")
    def __str__(self):
        return self.country_name
