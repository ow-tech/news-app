from flask import render_template, request, redirect, url_for
from . import main
# from app import app
from ..request import get_sources, get_articles
from ..models import Source, Articles

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting Sources

    # sources_name = get_sources('name')
    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')


    return render_template('index.html', General= general_news, Business = business_news, Entertainment = entertainment_news, Sports = sports_news, Technology = technology_news, Science = science_news, Health = health_news)
@main.route('/articles/<source_id>')
def articles(source_id):

    source_id = get_articles(source_id)
    title = f'{source_id} | All Articles'

    return render_template('articles.html', name= source_id, title = title)
