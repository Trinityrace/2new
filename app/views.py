from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news
# from . import News

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # message = 'World news today!'
    # return render_template('index.html',message = message)
    headline_news=get_news()
    print(headline_news)
    return render_template('headline.html',headlines=headline_news)

# @app.route('/article/<int:article_id>')
@main.route('/articles/<news_id>&<int:per_page>')
def article(article_id,per_page):

    '''
    View movie page function that returns the article details page and its data based on sources
    '''
    articles_source = get_articles(news_id, per_page)
    title = f'{articles_id} | All Articles'
    return render_template('article.html', title=title, name = articles_id, news= articles_source)