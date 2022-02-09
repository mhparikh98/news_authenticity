import logging
from abc import ABC, abstractmethod
from news_feed.models import NewsData, Category

logger = logging.getLogger("news_authenticity")


class BaseApiService(ABC):

    news_data = []

    def __init__(self):
        self.categories = list(
            Category.objects.all().values_list('name', flat=True))

    @abstractmethod
    def fetch_api_data(self):
        pass

    def save_data(self):
        try:
            for data in self.news_data:
                news_list = list(data.values())[0]
                news_feeds = [
                    NewsData(title=news.get('title'),
                             url=news.get('url'),
                             content=news.get('content'),
                             category=news.get('category'))
                    for news in news_list if NewsData.objects.filter(url=news.get('url')).count() == 0
                ]
                NewsData.objects.bulk_create(news_feeds)
        except Exception as e:
            logger.error(
                dict(
                    message="Exception to save data to database",
                    class_name="BaseApiService",
                    method_name="save_data",
                    errors=e,
                )
            )
