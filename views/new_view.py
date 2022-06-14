from flask import render_template
from models import News

def news():
    all_news = News.get_all_news()
    return render_template('en/news.html',news =all_news)