from django.urls import path,include
from . import views


app_name = "perfil"
urlpatterns = [
    path("", views.perfil, name = "perfil"),
]