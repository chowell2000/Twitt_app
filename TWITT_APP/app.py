"""Code for flask app
"""

from flask import Flask
from .models import DB


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitt Off!'

    @app.route('/about')
    def about():
        return "about me"
    return app
