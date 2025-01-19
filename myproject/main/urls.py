from django.urls import path
from . import views

urlpatterns = [
    path("", views.profession, name="profession"),
  
]