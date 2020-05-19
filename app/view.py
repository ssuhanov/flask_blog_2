from flask import render_template

from app import app


@app.route('/')
def index():
    user_name = 'Username'
    return render_template('index.html', name=user_name)
