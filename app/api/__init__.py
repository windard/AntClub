# coding=utf-8

from flask import Blueprint

api = Blueprint('api', __name__)

from app.api.errors import *
from app.api.views import *
