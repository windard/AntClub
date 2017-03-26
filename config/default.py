# coding=utf-8

import os
from whoosh.analysis import StemmingAnalyzer

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(40)

    # SQLALCHEMY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True

    WHOOSH_BASE = os.path.join(basedir, 'db/whoosh_index')
    WHOOSH_ANALYZER = StemmingAnalyzer()

    # MAIL
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    XDANT_MAIL_SUBJECT_PREFIX = '[XDANT]'
    XDANT_MAIL_SENDER = os.environ.get('XDANT_MAIL_SENDER') or MAIL_USERNAME

    # XDANT
    XDANT_ADMIN = os.environ.get('XDANT_ADMIN')
    XDANT_POSTS_PER_PAGE = 20
    XDANT_FOLLOWERS_PER_PAGES = 30
    XDANT_COMMENTS_PER_PAGE = 50
    XDANT_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    THREADED = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://web:web@localhost/xdant'
