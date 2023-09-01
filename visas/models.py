from django.db import models

class Entry(models.Model):
    citizen_country = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    visa_needed = models.BooleanField(default=True)

    def __str__(self):
        return self.home_country
#enka42!!