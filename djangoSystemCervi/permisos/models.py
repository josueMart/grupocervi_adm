from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Permission(models.Model):
	date = models.DateField(auto_now=True)
	asks = models.CharField(max_length=255)
	reason = models.CharField(max_length=255)
	reference = models.CharField(max_length=255)

	def __str__(self):
		return self.asks
