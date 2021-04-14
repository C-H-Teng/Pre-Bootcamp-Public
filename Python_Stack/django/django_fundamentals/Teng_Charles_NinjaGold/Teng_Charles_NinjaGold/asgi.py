"""
ASGI config for Teng_Charles_NinjaGold project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Teng_Charles_NinjaGold.settings')

application = get_asgi_application()
