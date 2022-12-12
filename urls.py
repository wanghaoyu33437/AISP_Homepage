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

    app.add_url_rule('/manage/member/member_all', endpoint='manage.member.member_all', view_func=manage_view.MMember.member)
    app.add_url_rule('/manage/member/member_par', endpoint='manage.member.member_par', view_func=manage_view.MMember.member_par)
    app.add_url_rule('/manage/member/member_info', endpoint='manage.member.member_info', view_func=manage_view.MMember.member_info)
    app.add_url_rule('/manage/member/member_img_upload', endpoint='manage.member.member_img_upload', view_func= manage_view.MMember.member_img_upload,methods=['POST'])
    app.add_url_rule('/manage/member/member_new', endpoint='manage.member.member_new',view_func=manage_view.MMember.member_new)
    app.add_url_rule('/manage/member/member_add', endpoint='manage.member.member_add',view_func=manage_view.MMember.member_add, methods=['POST'])
    app.add_url_rule('/manage/member/member_delete', endpoint='manage.member.member_delete', view_func= manage_view.MMember.member_delete,methods=['POST'])
    app.add_url_rule('/manage/member/member_update', endpoint='manage.member.member_update',view_func=manage_view.MMember.member_update, methods=['POST'])


    app.add_url_rule('/manage/publication/publication_all', endpoint='manage.publication.publication_all', view_func=manage_view.MPublication.publication)
    app.add_url_rule('/manage/publication/publication_par', endpoint='manage.publication.publication_par', view_func=manage_view.MPublication.publication_par)
    app.add_url_rule('/manage/publication/publication_info', endpoint='manage.publication.publication_info', view_func=manage_view.MPublication.publication_info)
    app.add_url_rule('/manage/publication/publication_delete', endpoint='manage.publication.publication_delete', view_func=manage_view.MPublication.publication_delete,methods=['POST'])
    app.add_url_rule('/manage/publication/publication_new', endpoint='manage.publication.publication_new',view_func=manage_view.MPublication.publication_new)
    app.add_url_rule('/manage/publication/publication_add', endpoint='manage.publication.publication_add', view_func=manage_view.MPublication.publication_add,methods=['POST'])
    app.add_url_rule('/manage/publication/publication_update', endpoint='manage.publication.publication_update',view_func=manage_view.MPublication.publication_update,methods=['POST'])




