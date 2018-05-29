from django.contrib import admin

# Register your models here.
from apps.state.models import State

admin.site.register(State)
