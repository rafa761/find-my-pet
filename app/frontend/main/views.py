# coding=utf-8

from flask import render_template, redirect, url_for, flash
from flask_login import logout_user

from app.frontend.main import main


@main.route('/')
def index():
	return render_template('home.html')


@main.route('/logout')
def logout():
	logout_user()
	flash('You have logged out')
	return redirect(url_for('index'))
