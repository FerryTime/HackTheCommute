"""
WSGI config for hackthecommute project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackthecommute.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Heroku for static files
# https://devcenter.heroku.com/articles/getting-started-with-django#start-a-django-app-inside-a-virtualenv
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

# Heroku stuff

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
