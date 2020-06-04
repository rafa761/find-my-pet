# coding=utf-8

from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import logout_user
from flask_security import current_user

from app.frontend.views import main_blueprint


@main_blueprint.route('/')
def index():
	return render_template('index.html')


@main_blueprint.route('/about')
def about():
	return render_template('about.html')


@main_blueprint.route('/logout')
def logout():
	logout_user()
	flash('You have logged out')
	return redirect(url_for('index'))
