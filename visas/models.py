from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Entry(models.Model):

    def __str__(self):
        return self.country_cit

    country_cit = models.CharField(max_length=100)
    country_dest = models.CharField(max_length=100)
    visa_needed = models.BooleanField(default=True)
