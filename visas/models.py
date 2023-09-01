from django.db import models
from django.utils.translation import gettext_lazy as _


class Entry(models.Model):
    class VisaType(models.TextChoices):
        VISA_FREE = "VF", _("Visa Free")
        VISA_ON_ARRIVAL = "VOA", _("Visa on Arrival (including eTA)")
        VISA_REQUIRED = "VR", _("Visa Required")
        COVID_BAN = "CB", _("Covid Ban")
        NO_ADMISSION = "NA", _("No Admission")
        UNKNOWN = "??", _("Unknown")
        
    citizen_country = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=3,
                                 choices=VisaType.choices,
                                 default=VisaType.UNKNOWN)

    def __str__(self):
        return self.citizen_country
#enka42!!