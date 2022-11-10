from django.urls import re_path

from . import websocketsConsumer


#aca llegan las peticiones ws
websocket_urlpatterns = [
    re_path("", websocketsConsumer.Comsumidor.as_asgi()),
]