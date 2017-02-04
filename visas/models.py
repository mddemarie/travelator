from django.db import models

# Create your models here.
class Entry(models.Model):
    country_cit = models.CharField(max_length=100)
    country_dest = models.CharField(max_length=100)
    visa_needed = models.BooleanField(default=True)
