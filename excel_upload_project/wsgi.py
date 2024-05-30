"""
WSGI config for excel_upload_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

application = get_wsgi_application()

# Add below lines to start the server with specified configurations
from django.core.servers.basehttp import get_internal_wsgi_application
from django.core.management.commands.runserver import Command

Command.default_port = os.environ.get('PORT', '8000')
server = get_internal_wsgi_application()
