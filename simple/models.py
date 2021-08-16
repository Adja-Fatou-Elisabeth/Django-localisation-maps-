from django import forms
from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()

