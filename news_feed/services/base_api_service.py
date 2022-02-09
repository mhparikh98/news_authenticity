import logging
from abc import ABC, abstractmethod
from news_feed.models import NewsData, Category

logger = logging.getLogger("news_authenticity")


class BaseApiService(ABC):
    """
    Generated the Base API class so that we can define the derived class in which we are calling the repected api.
    """

    news_data = []

    def __init__(self):
        self.categories = list(
            Category.objects.all().values_list('name', flat=True))

    @abstractmethod
    def fetch_api_data(self):
        pass

    def save_data(self):
        """
        After fetching the data we are saving data to the database.
        """
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
