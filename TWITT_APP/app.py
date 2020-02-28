"""Code for flask app
"""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User


def create_app():
    app = Flask(__name__)

# Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

# stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Tell the app about the database
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home',
                               users=users)

    @app.route('/about')
    def about():
        return "about me"

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])

    return app
