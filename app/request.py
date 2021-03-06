import urllib.request,json
# from app import app
from .models import Newws, Articles

# # News = news.News
# # Getting api key
# api_key = app.config['NEWS_API_KEY']
# # Getting the news base url
# base_url = app.config["NEWS_API_BASE_URL"]

api_key = None
base_url = None

newws_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['TOP_HEADLINES_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_articles(articles_list):
    '''
    Function that processes the json results for the articles
    '''
    articles_location_list = []

    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt=article.get('publishedAt')
        content=article.get('content')

        if urlToImage:
            articles_source_object = Articles(author, title, description, url, urlToImage,publishedAt,content)
            articles_location_list.append(articles_source_object)

    return articles_location_list