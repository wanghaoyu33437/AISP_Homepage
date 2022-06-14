from flask import Flask,session,request
import urls
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from ext import db
from flask import render_template,redirect,url_for
app = Flask(__name__)
# 路由
urls.route(app)
# 模板更改后立即生效
app.jinja_env.auto_reload = True
app.config.from_object(BaseConfig)
db.init_app(app)

@app.errorhandler(404)  # 传入错误码作为参数状态
def error_date(error):  # 接受错误作为参数
    return render_template('404.html'),404
@app.errorhandler(500)  # 传入错误码作为参数状态
def error_date(error):  # 接受错误作为参数
    return render_template('500.html'),404

@app.before_request
def before_user():
    if request.path.startswith("/static"):
        return None
    if request.path.startswith("/manage"):
        if not session.get("username"):
            return redirect(url_for('admin.admin'))



if __name__ == '__main__':
    app.run()


