from django.urls import path,include
from . import views


app_name = "torneos"
urlpatterns = [
    path("", views.torneos, name = "torneos"),
]