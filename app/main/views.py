# coding=utf-8

from datetime import datetime
from flask_login import login_required, current_user, logout_user, current_user, login_user
from flask_sqlalchemy import get_debug_queries
from flask import render_template, session, redirect, url_for, abort, flash, request, current_app, make_response, jsonify

from . import main
from ..models import User
from .. import db
from .forms import LoginForm, RegistrationForm, ChangeEmailForm, ChangePasswordForm, PasswordResetRequestForm, PasswordResetForm

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/data")
def data():
    return render_template("data.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/blog")
def blog():
    return render_template("blog.html")

@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            # flash("Log In Successful ~","success")
            return redirect(url_for('main.admin'))
        flash('Invalid username or password','danger')
        return redirect(url_for('main.login'))
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('You have been logged out','warning')
    return redirect(url_for('main.index'))

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            return redirect(url_for("main.register"))
        else:
            flash("Register Successful ~ ", "success")
            return redirect(url_for("main.login"))
    return render_template('register.html', form=form)

@main.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

@main.route("/edit")
def edit():
    return render_template("edit.html")