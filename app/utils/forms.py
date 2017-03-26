# coding=utf-8

from flask import current_app, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import validate_csrf
from flask_login import login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired, ValidationError

from app import db
from app.models import User
from app.utils import response_dict
from app.utils.constants import EMAIL_INVALID, PASSWORD_NOT_MATCH, DATA_REQUIRED, EMAIL_USED, USERNAME_USED, \
    CSRF_INVALID
from app.utils.validators import NickName, EqualTo

class Form(FlaskForm):
    """docstring for Form"""

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

    def error_detail(self):
        for key in self.errors:
            for error_code in self.errors[key]:
                if isinstance(error_code, int):
                    response = response_dict(error_code)
                    return response

    def validate_csrf_token(self, field):
        if not self.csrf_enabled:
            return True
        if hasattr(request, 'csrf_valid') and request.csrf_valid:
            # this is validated by CsrfProtect
            return True
        if not validate_csrf(field.data, self.SECRET_KEY, self.TIME_LIMIT):
            raise ValidationError(CSRF_INVALID)


class SessionForm(Form):
    """docstring for LoginForm"""
    email = StringField('Email', validators=[Email(EMAIL_INVALID)])
    password = PasswordField('Password')

    def login(self):
        entity = User.query.filter_by(email=self.email.data).first()
        if entity is not None and entity.verify_password(self.password.data):
            login_user(entity)
            identity_changed.send(current_app._get_current_object(), identity=Identity(entity.get_id()))
            return True
        return False

    @staticmethod
    def logout():
        logout_user()
        identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())


class RegistrationForm(Form):
    """docstring for RegistrationForm"""
    email = StringField('Email', validators=[Email(EMAIL_INVALID)])
    username = StringField('Username', validators=[NickName()])
    password = PasswordField('Password',
                             validators=[DataRequired(DATA_REQUIRED), EqualTo('password2', message=PASSWORD_NOT_MATCH)])
    password2 = PasswordField('Confirm password', validators=[DataRequired(DATA_REQUIRED)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(EMAIL_USED)

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(USERNAME_USED)

    def register(self):
        user = User(username=self.username.data, email=self.email.data, password=self.password.data)
        db.session.add(user)
        db.session.commit()
        user.send_mail()
        return user
