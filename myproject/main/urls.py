from django.urls import path
from . import views

urlpatterns = [
    path("", views.profession, name="profession"),
    path("genstatistic/", views.statistic, name="statistic"),
]