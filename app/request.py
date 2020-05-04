from app import app
from .models import news
import urllib.request, json

News = news.News
Articles = news.Articles

api_key = app.config["NEWS_API_URL"]
# print(api_key)
base_url = app.config["NEWS_API_BASE_URL"]
articles_url = app.config["NEWS_API_ARTICLES_URL"]
# print(base_url)