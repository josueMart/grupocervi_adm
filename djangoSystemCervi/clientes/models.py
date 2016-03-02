from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	contactName = models.CharField(max_length=255)
	telephoneNumber = models.CharField(max_length=10)
	email = models.EmailField(max_length=254)
	deliveryAddres = models.CharField(max_length=255)
	rfc = models.CharField(max_length=255)
	salesPerson = models.CharField(max_length=255)
	observations = models.TextField(max_length=400)

	def __str__(self):
		return self.name



