from django.db import models

# Create your models here.
from apps.city.models import City
from apps.location.models import Location
from apps.state.models import State
from apps.suburb.models import Suburb


class Userinfo(models.Model):
    USER_TYPES = (
        ('Promotor', 'Promotor'),
        ('Invitado', 'Invitado'),
    )

    AGENT_TYPE = (
        ('Representante de Casilla', 'Representante de Casilla'),
        ('Representante de Voto', 'Representante de Voto'),
        ('Observador Electoral', 'Observador Electoral'),
        ('Promotor del Voto', 'Promotor del Voto'),
        ('Representante Seccional', 'Representante Seccional'),
        ('Representante de Localidad', 'Representante de Localidad'),
        ('Representante de Colonia', 'Representante de Colonia'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ine = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=20)
    street_between = models.CharField(max_length=100)
    street_and_between = models.CharField(max_length=100)
    suburb = models.ForeignKey(Suburb, on_delete=models.CASCADE)
    locality = models.ForeignKey(Location, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    agent_type = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return '{}'.format(self.first_name, self.last_name)
