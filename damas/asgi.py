import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'damas.settings')
django_asgi_app = get_asgi_application()

from . import websockets_urls

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websockets_urls.websocket_urlpatterns))
    ),
    # Just HTTP for now. (We can add other protocols later.)
})
