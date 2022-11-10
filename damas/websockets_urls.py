from django.urls import re_path, include

from . import websocketsConsumer


#aca llegan las peticiones ws
websocket_urlpatterns = [
    re_path("", websocketsConsumer.OnLine.as_asgi()),
]