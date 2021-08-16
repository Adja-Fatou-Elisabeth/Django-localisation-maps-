from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.translation import ugettext as _
import googlemaps
from django.views.generic import CreateView, DetailView, RedirectView, UpdateView, ListView,FormView, DeleteView
from simple.forms import MyLocationForm
from simple.models import MyLocationModel
from django.urls import reverse


class LocationCreate(CreateView): 
    form_class = MyLocationForm
    redirect_field_name= "next"
    view_name = "create"
    template_name= "create.html"
           
    def get_success_url(self):
           return reverse("simple:index")
   

class LocationView(ListView): 
    form_class = MyLocationForm
    redirect_field_name= "next"
    view_name = "index"
    template_name= "index.html"

    def get_queryset(self):
        return MyLocationModel.objects.all()

    def get_success_url(self):
           return reverse("simple:index")
   

