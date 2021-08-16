""" from django import forms
from django.db import models
from places.fields import PlacesField


class MyLocationModel(models.Model):
    location = PlacesField()


class distance(forms.Form):
    pickupAddress = forms.Field(label=**'pickup address')**
    destAddress = forms.Field(label=**'destination address'**)

 """
from django import forms  
from .models import MyLocationModel

class MyLocationForm(forms.ModelForm):  
    class Meta:  
        model = MyLocationModel
        fields = "__all__"
