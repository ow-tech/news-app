from app import app
import urllib.request, json
from .models import source


Source = source.Source


#Getting api Key
api_key = app.config['NEWS_API_KEY']

#Getting the Source base url
base_url = app.config["SOURCE_BASE_URL"]


def get_sources(category):
    """
    function that gets the sources
    """

    get_source_url = base_url.format(category, api_key)


    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read
        get_source_response = json.loads(get_source_data)

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


        if url:
            source_object = Source(name, category, country, language, description, url)
            source_results. append(source_object)

    return source_results
