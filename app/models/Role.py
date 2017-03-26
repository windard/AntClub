# coding=utf-8

from app import db, login_manager

import bleach
import hashlib
from markdown import markdown
from datetime import datetime
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Permission(object):
    WRITE_ARTICLES = 0x01
    WRITE_DATAS = 0x02
    MODERATE_ARTICLES = 0x04
    MODERATE_DATAS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permission = db.Column(db.Integer)

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.WRITE_ARTICLES |
                     Permission.WRITE_DATAS, True),
            'Moderator': (Permission.WRITE_ARTICLES |
                          Permission.WRITE_DATAS |
                          Permission.MODERATE_ARTICLES |
                          Permission.MODERATE_DATAS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permission = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name
