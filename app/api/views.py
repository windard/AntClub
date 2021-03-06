# coding=utf-8

from flask import request, jsonify

from app.api import api
from app.utils import response_dict
from app.utils.forms import SessionForm, RegistrationForm
from app.utils.constants import SUCCESS, LOGIN_FAILED


@api.route('/sessions', methods=['POST', 'DELETE'])
def sessions():
    if request.method == 'POST':
        form = SessionForm()
        if not form.validate():
            return jsonify(form.error_detail())
        if form.login():
            return jsonify(response_dict(SUCCESS))
        else:
            return jsonify(response_dict(LOGIN_FAILED))
    else:
        SessionForm.logout()
        return jsonify(response_dict(SUCCESS))


@api.route("/register", methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        form.register()
        return jsonify(response_dict(SUCCESS))
    return jsonify(form.error_detail())
