from django.db import models

class Entry(models.Model):
	country_cit = models.Charfield(max_length=50)
	country_dest = models.Charfield(max_length=50)
	visa_needed = models.BooleanField(default=None)
# Create your models here.
