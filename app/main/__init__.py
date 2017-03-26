# coding=utf-8

from flask import Blueprint

main = Blueprint('main', __name__)

from app.main.errors import *
from app.main.views import *
