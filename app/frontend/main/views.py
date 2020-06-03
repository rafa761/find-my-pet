# coding=utf-8

from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import logout_user
from flask_security import current_user

from app.backend.web.business.pet import PetBus
from app.backend.web.business.pet_status import PetStatusBus
from app.backend.web.business.pet_type import PetTypeBus
from app.frontend.main import main


@main.route('/')
def index():
	return render_template('index.html')


@main.route('/about')
def about():
	return render_template('about.html')


@main.route('/logout')
def logout():
	logout_user()
	flash('You have logged out')
	return redirect(url_for('index'))
