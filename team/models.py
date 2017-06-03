# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator,EmailValidator

# Create your models here.

class Members(models.Model):

	ROLE_CHOICES=(
		(0,'Member'),
		(1,'Admin')
	)

	phn_rgx = RegexValidator(regex=r'^[7-9]\d{9}$', message="Phone number must be entered in the format: '9999999999'. 10 digits allowed.")
	email_validator = EmailValidator(message= "Wrong email ")
	first_name = models.CharField(max_length=100, blank=True, default='')
	last_name = models.CharField(max_length=100, blank=True, default='')
	phone = models.CharField(validators=[phn_rgx],max_length=10,blank = True)
	email = models.CharField(validators=[email_validator],max_length = 254, blank = True)
	role = models.IntegerField(choices=ROLE_CHOICES, default=0)
