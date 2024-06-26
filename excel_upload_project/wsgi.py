"""
WSGI config for excel_upload_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# wsgi.py

import os
from django.core.wsgi import get_wsgi_application
from django.core.servers.basehttp import get_internal_wsgi_application
from django.core.management.commands.runserver import Command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "excel_upload_project.settings")

application = get_wsgi_application()

Command.default_port = os.environ.get('PORT', '8000')
server = get_internal_wsgi_application()
