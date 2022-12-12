from flask import render_template,request,redirect,url_for,session,jsonify,app

from ext import db
from models import Admin,Member,Publications

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



class MMember:
    @staticmethod
    def member_par():
        return render_template('manage/member/member_par.html')
    @staticmethod
    def member():
        members = Member.query.order_by(Member.id).all()
        return render_template('manage/member/member.html',members=members)
    @staticmethod
    def member_info():
        ID = request.args['ID']
        members = Member.query.filter_by(id=ID).all()
        # print(members[0])
        return render_template('manage/member/member_info.html',member= members[0])
    @staticmethod
    def member_img_upload():
        if request.method == 'POST':
            file = request.files['file']
            name = request.values['name']
            if name=='undefined' or name=='':
                return jsonify({'state':'请先填写上述选项'})
            # # file_name=  request.args['image_name']
            file.save(f'static/images/members/{name}.png')
        return jsonify({'state':'success','name':name})
    @staticmethod
    def member_new():
        return render_template('manage/member/member_info.html')
    @staticmethod
    def member_add():
        print(request.form)
        if request.method == 'POST':
            name = request.form['name']
            en_name = request.form['en_name']
            type = request.form['type']
            title = request.form['title']
            file = request.form['file']
            url = request.form['url']
            if name!='' and en_name!='' and type!=''and title!='' and url !='':
                member = Member(name=name, en_name=en_name, type=type, title=title,img='',url=url)
                db.session.add(member)
                db.session.commit()
            else:
                return render_template('manage/member/member_info.html',error='添加失败，请填写全部选项')
        # db.session.commit()
        return render_template('manage/member/member_info.html')
    @staticmethod
    def member_delete():
        # print(request)
        if request.method == 'POST':
            ID = request.values['ID']
            # file_name=  request.args['image_name']
            # print(ID)
            Member.query.filter(Member.id == ID).delete()
            db.session.commit()
        return jsonify({'state':'success'})
    @staticmethod
    def member_update():
        # print(request)
        if request.method == 'POST':
            ID = request.values['ID']
            name = request.form['name']
            en_name = request.form['en_name']
            type = request.form['type']
            title = request.form['title']
            file = request.form['file']
            url = request.form['url']
            Member.query.filter(Member.ID == ID).update(
                {'name': name, 'en_name': en_name, 'type': type,
                 'title': title, 'url': url})
            db.session.commit()
            # file_name=  request.args['image_name']
            # print(ID)
            # Member.query.filter(Member.id == ID).delete()
            #             # db.session.commit()
        return "<h3>修改成功！请关闭刷新....</h3>"

class MPublication:
    @staticmethod
    def publication_par():
        return render_template('manage/publication/publication_par.html')
    @staticmethod
    def publication():
        publications = Publications.query.order_by(Publications.year).all()
        return render_template('manage/publication/publication.html',publications=publications)
    @staticmethod
    def publication_info():
        ID = request.args['ID']
        publications = Publications.query.filter_by(id=ID).all()
        # print(members[0])
        return render_template('manage/publication/publication_info.html',publication= publications[0])
    @staticmethod
    def publication_add():
        print(request.form)
        if request.method == 'POST':
            title = request.form['title']
            conference = request.form['conference']
            year = request.form['year']
            authors = request.form['authors']
            tag = request.form['tag']
            url = request.form['url']
            if title != '' and conference != '' and year != '' and authors != '' and tag != '':
                publication = Publications(title=title, conference=conference, year=year, authors=authors, tag=tag, url=url)
                db.session.add(publication)
                db.session.commit()
            else:
                return render_template('manage/publication/publication_info.html', error='添加失败，请填写全部选项')
        # db.session.commit()
        return render_template('manage/publication/publication_info.html')
    @staticmethod
    def publication_new():
        return render_template('manage/publication/publication_info.html')
    @staticmethod
    def publication_delete():
        # print(request)
        if request.method == 'POST':
            ID = request.values['ID']

            # file_name=  request.args['image_name']
            # print(ID)
            Publications.query.filter(Publications.id == ID).delete()
            db.session.commit()
        return jsonify({'state':'success'})
    @staticmethod
    def publication_update():
        # print(request)
        if request.method == 'POST':
            print(request.form)
            ID = request.values['ID']
            title = request.form['title']
            conference = request.form['conference']
            year = request.form['year']
            authors = request.form['authors']
            tag = request.form['tag']
            url = request.form['url']
            Publications.query.filter(Publications.ID == ID).update({'title': title,'conference':conference,'year':year,
                                                                      'authors':authors,'tag':tag,'url':url})
            db.session.commit()
            # file_name=  request.args['image_name']
            # print(ID)
            # Member.query.filter(Member.id == ID).delete()
            #             # db.session.commit()
        return "<h3>修改成功！请关闭刷新....</h3>"