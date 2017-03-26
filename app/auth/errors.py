# coding=utf-8

from flask import render_template, request, jsonify

from app.auth import auth

from app.utils import ValidationError


@auth.app_errorhandler(403)
def forbidden(e):
    return forbidden('')


@auth.app_errorhandler(404)
def page_no_found(e):
    return not_found(request.url)


@auth.app_errorhandler(500)
def internal_server_error(e):
    return error_handler('internal server error', '', 500)


def error_handler(error, message, code):
    response = jsonify({'error': error, 'message': message})
    response.status_code = code
    return response


def not_found(message):
    response = jsonify({'error': 'not found', 'message': message})
    response.status_code = 404
    return response


def forbidden(message):
    response = jsonify({"error": "forbidden", "message": message})
    response.status_code = 403
    return response


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({"error": "unauthorized", "message": message})
    response.status_code = 401
    return response


@auth.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
