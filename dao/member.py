from ext import db


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.VARCHAR, )
    type = db.Column(db.VARCHAR, )
    title = db.Column(db.VARCHAR, )
    img = db.Column(db.VARCHAR, )
    url = db.Column(db.VARCHAR, )

    def __init__(self, name, type, title, img,url):
        self.name = name
        self.type = type
        self.title = title
        self.img = img
        self.url = url
