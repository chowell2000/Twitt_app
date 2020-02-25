import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    """Twitter Users we will analyze

    Arguments:
        DB {string} -- User name
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(20), nullable=False)


class Tweet(DB.Model):
    """Tweets we pull to analyze

    Arguments:
        DB {string} -- Tweet text
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
