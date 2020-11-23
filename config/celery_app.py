import os

from environ import Env as get_env
from celery import Celery


env = get_env()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
app = Celery("had")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
# Load the beat tasks

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
