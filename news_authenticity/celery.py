from django.conf import settings
from celery import Celery
from environs import Env

env = Env()
env.read_env(".env")

app = Celery('news_authenticity')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
