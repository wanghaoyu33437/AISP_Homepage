import calendar
from ext import db
from sqlalchemy.sql import func
from flask import Markup

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.VARCHAR, )
    en_name = db.Column(db.VARCHAR, )
    type = db.Column(db.VARCHAR, )
    title = db.Column(db.VARCHAR, )
    img = db.Column(db.VARCHAR, )
    url = db.Column(db.VARCHAR, )
    def __init__(self, name,en_name, type, title, img,url):
        self.name = name
        self.type = type
        self.title = title
        self.img = img
        self.url = url
        self.en_name = en_name
class News(db.Model):
    __tablename__ = 'new'
    id = db.Column(db.Integer, primary_key=True, )
    info = db.Column(db.VARCHAR)
    detail = db.Column(db.VARCHAR)
    date = db.Column(db.DATE,default= func.now())
    type = db.Column(db.VARCHAR)
    def __init__(self, info, detail, type):
        self.info = info
        self.date = func.now()
        self.detail = detail
        self.type = type
    @staticmethod
    def get_top_x_news(x=5):
        news = News.query.order_by(News.date.desc()).limit(x).all()
        for d in news:
            date = str(d.date)
            Y, M, D = date.strip().split('-')
            d.date = Markup("<h5>%s</h5><h3>%s</h3><h5>%s.</h5>" % (Y, D, calendar.month_abbr[int(M)]))
        return news
    @staticmethod
    def get_all_news():
        news = News.query.order_by(News.date.desc()).all()
        for d in news:
            date = str(d.date)
            Y, M, D = date.strip().split('-')
            d.date = "%s %dth, %s"%(calendar.month_abbr[int(M)],int(D),Y)
        return news
class Publications(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True, )
    title = db.Column(db.VARCHAR)
    conference = db.Column(db.VARCHAR)
    year = db.Column(db.DATE,default= func.now())
    authors = db.Column(db.VARCHAR)
    tag = db.Column(db.VARCHAR)
    create_time = db.Column(db.DATETIME)
    def __init__(self, title, conference, year,authors,tag,url):
        self.title = title
        self.conference = conference
        self.year = year
        self.authors = authors
        self.tag = tag
        self.url = url
    @staticmethod
    def get_all_publications():
        publications = Publications.query.order_by(Publications.create_time.desc()).all()
        return publications


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR )
    password = db.Column(db.VARCHAR )