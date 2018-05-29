from django.db import models


# Create your models here.
class State(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
