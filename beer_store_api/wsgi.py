"""
WSGI config for beer_store_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys


sys.path.append('/home/djuta/webapps/beer_store_api/beer_store_api')

os.environ["DJANGO_SETTINGS_MODULE"] = "beer_store_api.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
