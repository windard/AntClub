# coding=utf-8

from config.default import Config


class TestingConfig(Config):
    SERVER_NAME = 'localhost'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
