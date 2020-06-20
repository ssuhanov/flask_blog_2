from flask import render_template

from app import app


@app.route('/')
def index():
    user_name = 'Username'
    return render_template('index.html', name=user_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
