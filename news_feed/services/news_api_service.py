import logging
import requests
from datetime import datetime
from http import HTTPStatus
from news_feed.services.base_api_service import BaseApiService
from news_feed.constants import NewsApiConstants
from news_feed.models import Category
from news_feed.tasks.send_notification_task import send_notification_email

logger = logging.getLogger("news_authenticity")


class NewsApiService(BaseApiService):

    def __init__(self):
        """
        Initializing the paramas for the news api
        """
        BaseApiService.__init__(self)
        self.url = NewsApiConstants.NEWS_API_ORG_URL
        self.today = datetime.today().date().strftime("%Y-%m-%d")
        self.params = {
            "from": self.today,
            "sort_by": "popularity",
            "apikey": NewsApiConstants.NEWS_API_ORG_API_KEY
        }

    def fetch_api_data(self):
        """
        calling the news api and then extracting the data from the response of the API, also generating the task to send email notification.
        """
        try:
            for category in self.categories:
                category_obj = Category.objects.filter(name=category).first()
                param = self.params.copy()
                param.update({"q": category})
                resp = requests.get(self.url, param)
                json_resp = resp.json()

                if json_resp.get('status') == HTTPStatus.OK.phrase.lower():
                    articles = json_resp.get('articles')
                    article_data = [
                        {"category": category_obj, "title": article.get('title', ''), "content": article.get(
                            'content', ''), "url": article.get('url', '')} for article in articles]
                    self.news_data.append({category_obj.name: article_data})
                    if articles:
                        send_notification_email.delay(category)
                else:
                    logger.info(
                        dict(
                            message=f"Error response for url : {self.url}, category : {category}, response : {json_resp}",
                            class_name="NewsApiService",
                            method_name="fetch_api_data",
                        )
                    )

        except Exception as e:
            logger.error(
                dict(
                    message="Exception in NewsApiService method",
                    class_name="NewsApiService",
                    method_name="fetch_api_data",
                    errors=e,
                )
            )
