from flask import render_template
from views import index_view,project_view,publication_view,member_view,new_view,activities_view,manage_view
import views
def route(app):
    app.add_url_rule('/',endpoint='index',view_func=index_view.index)
    app.add_url_rule('/projects', endpoint='projects', view_func=project_view.projects)
    app.add_url_rule('/members', endpoint='members', view_func=member_view.members)
    app.add_url_rule('/news', endpoint='news', view_func=new_view.news)
    app.add_url_rule('/publications', endpoint='publications', view_func=publication_view.publications)
    app.add_url_rule('/activities', endpoint='activities', view_func=activities_view.activities)

    app.add_url_rule('/admin/', endpoint='admin.admin', view_func=manage_view.admin,methods=['GET'])
    app.add_url_rule('/admin/login', endpoint='admin.login', view_func=manage_view.login,methods=['POST'])

    app.add_url_rule('/manage/main', endpoint='manage.main', view_func=manage_view.main)
    app.add_url_rule('/manage/welcome', endpoint='manage.welcome', view_func=manage_view.welcome)

