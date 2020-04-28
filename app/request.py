# from app import app
import urllib.request
import json
from .models import Source, Articles



# #Getting api Key
# api_key = app.config['NEWS_API_KEY']

# #Getting the Source base url
# base_url = app.config["SOURCE_BASE_URL"]


# #Getting Everything base url for articles
# articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']

api_key = None
sources_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_BASE_URL']
    articles_url = app.config['EVERYTHING_SOURCE_BASE_URL']



def get_sources(category):
    """
    function that gets the sources
    """

    get_source_url = base_url.format(category, api_key)
    print(get_source_url)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)


        sources_results = None

        if get_source_response['sources']:
            sources_results_list = get_source_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(source_list):
    '''
    Function that process the source results and transforms them to a list objects
    Args:
        source_list: A list of dictionaries that contains source details
    Returns:
        source_results: A list of source objects
    '''

    source_results = []

    for source_item in source_list:
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        url = source_item.get('url')
        description = source_item.get('description')
        name = source_item.get('name')
        source_id = source_item.get('id')


        if url:
            source_object = Source(name, category, country, language, description, url, source_id)
            source_results. append(source_object)

    return source_results


def get_articles(source_id):
    get_article_location_url = articles_url.format(source_id, api_key)

    with urllib.request.urlopen(get_article_location_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        articles_results = None

        if get_article_response['articles']:
            articles_results_list = get_article_response['articles']

            articles_results = process_articles(articles_results_list )

    return articles_results

def process_articles(obtained_articles):
    article_location_list = []

    for article in obtained_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        id = article.get('source.id')

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage,id)
            article_location_list.append(article_source_object)

    return article_location_list

