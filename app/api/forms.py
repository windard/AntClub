# coding=utf-8

from flask import current_app
from flask_login import login_user
from flask_principal import identity_changed, Identity
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError

from app.models import User
from app.utils.forms import Form
from app.utils.constants import EMAIL_INVALID, PASSWORD_INVALID, LOGIN_FAILED


class ChangePasswordForm(Form):
    """docstring for ChangePasswordForm"""
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password',
                             validators=[Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField("Update Password")


class PasswordResetRequestForm(Form):
    """docstring for PasswordResetRequestForm"""
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    """docstring for PasswordResetForm"""
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('New password',
                             validators=[Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[Required()])
    submit = SubmitField("Update Password")


class ChangeEmailForm(FlaskForm):
    """docstring for ChangeEmailForm"""
    email = StringField('New Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")
