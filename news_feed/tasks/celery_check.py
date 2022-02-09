import logging
from news_authenticity import celery_app
from celery import Task

logger = logging.getLogger("news_authenticity")


class CeleryExp(Task):

    name = "celery_check_task"

    def run(self, *args, **kwargs):
        logger.info("celery worked")


celery_check_task = celery_app.register_task(CeleryExp())
