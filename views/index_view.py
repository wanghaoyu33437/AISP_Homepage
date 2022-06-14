from flask import render_template
from models import News
import calendar
from flask import Markup


def format_date(data):
    for d in data:
        date = str(d.date)
        Y = date.Year(),
        print(Y)
def index():
    # news = News.query.order_by(News.date.desc()).all()
    # for d in news:
    #     date = str(d.date)
    #     Y,M,D = date.strip().split('-')
    #     d.date =Markup("<h5>%s</h5><h3>%s</h3><h5>%s.</h5>"%(Y,D,calendar.month_abbr[int(M)]))
    news = News.get_top_x_news(x=5)
    return render_template('en/index.html',news = news)