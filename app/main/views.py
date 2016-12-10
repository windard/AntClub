# coding=utf-8

from datetime import datetime
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from flask import render_template, session, redirect, url_for, abort, flash, request, current_app, make_response

from . import main

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

@main.route("/login")
def login():
	return render_template("login.html")

@main.route("/register")
def register():
	return render_template("register.html")

@main.route("/admin")
def admin():
	return render_template("admin.html")

@main.route("/edit")
def edit():
	return render_template("edit.html")