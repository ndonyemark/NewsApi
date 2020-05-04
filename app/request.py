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

def get_sources(category):
    
    get_news_source_url = base_url.format(category, api_key)
    print(get_news_source_url)
    with urllib.request.urlopen(get_news_source_url) as url:

        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_results = None

        if get_news_source_response['sources']:

            news_results_list = get_news_source_response["sources"]
            news_results = process_results(news_results_list)
    
    return news_results

def process_results(news_list):

    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name=news_item.get("name")
        description=news_item.get("description")
        url=news_item.get("url")
        category=news_item.get("category")
        language=news_item.get("language")
        country=news_item.get("country")

        if language == 'en':
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)
    
    return news_results