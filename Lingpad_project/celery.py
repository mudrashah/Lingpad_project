from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Lingpad_project.settings")
app = Celery("Lingpad_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
