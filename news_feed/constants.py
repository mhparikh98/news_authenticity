from django.conf import settings


class NewsApiConstants:
    BASE_NEWS_API = "https://newsapi.org"
    NEWS_API_ORG_URL = f"{BASE_NEWS_API}/v2/everything"
    NEWS_API_ORG_API_KEY = settings.NEWS_API_ORG_API_KEY
