# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class events(models.Model):
	title =  models.CharField(max_length = 150 ,blank=True,null=True)
	description =  models.CharField(max_length = 350 ,blank=True,null=True)
	completed = models.BooleanField(default=False)
	endTime = models.CharField(max_length = 150 )
	startTime = models.CharField(max_length = 150 )
	allDay = models.BooleanField(default=False)
	def __str__(self):
		return self.startTime
# Create your models here.
