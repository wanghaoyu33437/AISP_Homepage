from flask import render_template,request,redirect,url_for,session
import calendar
from flask import Markup
from models import Admin

def format_date(data):
    for d in data:
        date = str(d.date)
        Y = date.Year(),
        print(Y)
def main():
    return render_template('manage/main.html',)
def welcome():
    return render_template('manage/welcome.html',)
def admin():
    return render_template('manage/login.html',)

def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = Admin.query.filter_by(username=username).all()
        if len(user)!=0:
            pwd = user[0].password
            if password!=pwd:
                msg = "密码错误"
                return render_template('manage/login.html', msg=msg)
            session['username'] = username
            return redirect(url_for('manage.main'))
        else:
            msg="用户名不存在"
            return render_template('manage/login.html', msg=msg)