# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class insurance(models.Model):
	name= models.CharField(max_length=30)
	risks = models.ForeignKey(Risks)
	risks_type = models.ForeignKey(RisksType)
	risks_subtype = risk_type = models.ForeignKey(RisksSubType)
	data_field = models.ManyToManyField(insuranceData,through='Membership')

	class Meta:
		ordering=('name',)

	
class insuranceData(models.Model):
	CATEGORY_CHOICES = (('char', 'Character'),
                        ('num', 'Number'),
                        ('cure', 'Currency'),
			('date','Date'),)

	name = models.CharField(max_length=30)
        f_type = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	data = models.CharField(max_length=30)

class Risks(models.Model):
   
    Name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    class Meta:
        ordering = ('id',)

class RisksType(models.Model):

    Name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    risk = models.ForeignKey(Risks)
    class Meta:
        ordering = ('id',)


class RisksSubType(models.Model):

    Name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    risk_type = models.ForeignKey(RisksType)

    class Meta:
        ordering = ('id',)

