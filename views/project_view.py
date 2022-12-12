from flask import render_template
from models import Project

def projects():
    projects = Project.query.all()
    return render_template('en/projects.html',projects=projects)