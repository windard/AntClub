# coding=utf-8

from flask import Blueprint
from ..models import Permission
from .. import db
from ..models import Role

main = Blueprint('main', __name__)
from . import views, errors


@main.before_app_first_request
def create_database():
	db.create_all()
	Role.insert_roles()


@main.app_context_processor
def inject_permissions():
	return dict(Permission=Permission)
