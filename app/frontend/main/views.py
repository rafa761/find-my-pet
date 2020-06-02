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


@main.route('/pets')
def pets():
	pet_list = PetBus().get_all()

	return render_template('pets.html', pet_list=pet_list, current_user=current_user)


@main.route('/pet/add', methods=('GET', 'POST',))
def pet_add():
	if request.method == 'GET':
		pet_type_list = PetTypeBus().get()
		pet_status_list = PetStatusBus().get()
		return render_template('pet-add.html', pet_type_list=pet_type_list, pet_status_list=pet_status_list)

	try:
		response = jsonify(PetBus().add(request.form))

	except Exception as error:
		response = jsonify(str(error))
		response.status_code = 400

	flash('Successfuly saved Pet', category='message')
	return response


@main.route('/pet/edit', methods=('GET', 'POST',))
def pet_edit():
	pet_id = request.args.get('pet_id')

	if request.method == 'GET':
		pet_type_list = PetTypeBus().get()
		pet_status_list = PetStatusBus().get()

		pet_dict = PetBus().get_all(id=pet_id)
		return render_template('pet-edit.html', pet_dict=pet_dict[0], pet_type_list=pet_type_list,
		                       pet_status_list=pet_status_list)

	try:
		response = jsonify(PetBus().put(pet_id, request.form))

	except Exception as error:
		response = jsonify(str(error))
		response.status_code = 400

	flash('Successfuly edited Pet', category='message')
	return response


@main.route('/pet/delete', methods=('POST',))
def pet_delete():
	pet_id = request.args.get('pet_id')

	try:
		response = jsonify(PetBus().delete(pet_id))

	except Exception as error:
		response = jsonify(str(error))
		response.status_code = 400

	return response


@main.route('/logout')
def logout():
	logout_user()
	flash('You have logged out')
	return redirect(url_for('index'))
