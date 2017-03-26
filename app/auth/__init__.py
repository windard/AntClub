# coding=utf-8

from flask import Blueprint
from app.models import Role, User

auth = Blueprint('auth', __name__)

from app.auth import views, errors
