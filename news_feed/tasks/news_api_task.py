import logging
from celery import Task
from celery.schedules import crontab
from news_authenticity import celery_app
from news_feed.services.news_api_service import NewsApiService


celery_app.conf.beat_schedule.update(
    {
        "run-every-30mins": {
            "task": "news_api_task",
            "schedule": crontab(minute='*/1'),
        }
    }
)
logger = logging.getLogger("news_authenticity")


class NewsApiTask(Task):

    name = "news_api_task"

    def run(self):
        try:
            obj = NewsApiService()
            obj.fetch_api_data()
            obj.save_data()
        except Exception as e:
            logger.error(
                dict(
                    message="Exception in schedule reminder send mail task",
                    class_name="NewsApiTask",
                    errors=e,
                )
            )


news_api_task = celery_app.register_task(NewsApiTask())
