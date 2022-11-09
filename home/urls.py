from django.urls import path,include
from . import views


app_name = "home"
urlpatterns = [
    path("", views.home, name = "home"),
    path("login/", include("login.urls"), name = "login"),
    path("jugadores/", include("players.urls"), name = "jugadores"),
    path("torneos/", include("torneos.urls"), name = "torneos"),
    path("perfil/<str:name>", include("perfil.urls"), name = "perfil"),
]