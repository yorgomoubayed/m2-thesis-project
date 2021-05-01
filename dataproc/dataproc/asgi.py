"""
ASGI config for dataproc project.
Exposes the ASGI callable as a module-level variable named ``application``.
For more information on this file, see https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

# Python imports
import os

# Django imports
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataproc.settings')
application = get_asgi_application()
