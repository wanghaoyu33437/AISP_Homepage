from flask import render_template


def activities():
    return render_template('en/activities.html',activities=None)