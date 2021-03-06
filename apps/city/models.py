from django.db import models

# Create your models here.
from apps.state.models import State


class City(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)
