# coding=utf-8

from flask import request, jsonify

from app import  redis_store
from app.api import api
from app.utils import response_dict
from app.utils.forms import SessionForm, RegistrationForm
from app.utils.constants import SUCCESS, LOGIN_FAILED, LOGIN_OVERTIME


@api.route('/sessions', methods=['POST', 'DELETE'])
def sessions():
    if request.method == 'POST':
        form = SessionForm()
        if not form.validate():
            return jsonify(form.error_detail())
        if form.login():
            return jsonify(response_dict(SUCCESS))
        else:
            if redis_store.exists(request.remote_addr):
                if int(redis_store.get(request.remote_addr)) < 5:
                    redis_store.incr(request.remote_addr)
                else:
                    return jsonify(response_dict(LOGIN_OVERTIME))
            else:
                redis_store.incr(request.remote_addr)
                redis_store.expire(request.remote_addr, 10*60)
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
