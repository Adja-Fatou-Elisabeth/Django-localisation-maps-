from django.urls import path
import simple.views as views


app_name = "simple"
urlpatterns = [
    path('', views.LocationView.as_view(), name='index'),
    path('create/', views.LocationCreate.as_view(), name='create'),
]
