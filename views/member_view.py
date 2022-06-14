from flask import render_template
from ext import db

from models import Member
def members():
    teachers = Member.query.filter_by(type='teacher').all()
    phds = Member.query.filter_by(type='phd').all()
    mses = Member.query.filter_by(type='ms').all()
    bses = Member.query.filter_by(type = 'bs').all()
    xyes = Member.query.filter_by(type='xy').all()
    return render_template('en/members.html',teachers = teachers,mses=mses,phds=phds,bses=bses,xyes=xyes)