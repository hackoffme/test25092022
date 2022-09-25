"""
WSGI config for test_hh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_hh.settings')

application = get_wsgi_application()


from parse_doc.cron import my_scheduled_job
my_scheduled_job()
