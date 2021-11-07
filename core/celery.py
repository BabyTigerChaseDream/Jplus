import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINS_MODULE','core.settings')
app=Celery('core')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()