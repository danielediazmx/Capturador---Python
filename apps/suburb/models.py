from django.db import models

# Create your models here.
from apps.location.models import Location


class Suburb(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)
