"""
ASGI config for realtinic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import main.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtinic.settings')

app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                    *main.routing.websocket_urlpatterns
            ]
            )
        )
    )
})
