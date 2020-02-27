"""Code for flask app
"""

from decouple import config
from flask import Flask, render_template, request
from .models import DB



def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')

    @app.route('/about')
    def about():
        return "about me"
    return app
