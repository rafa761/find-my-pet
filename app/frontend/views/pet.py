# coding=utf-8

from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import logout_user
from flask_security import current_user

from app.backend.web.business.pet import PetBus
from app.backend.web.business.pet_status import PetStatusBus
from app.backend.web.business.pet_type import PetTypeBus
from app.frontend.views import pet_blueprint


@pet_blueprint.route('/pets')
def pets():
	pet_list = PetBus().get()

	return render_template('pets.html', pet_list=pet_list, current_user=current_user)


@pet_blueprint.route('/add', methods=('GET', 'POST',))
def pet_add():
	if request.method == 'GET':
		pet_type_list = PetTypeBus().get()
		pet_status_list = PetStatusBus().get()
		return render_template('pet-add.html', pet_type_list=pet_type_list, pet_status_list=pet_status_list)

	try:
		PetBus().add(request.form)
		flash('Successfuly saved Pet', category='message')
		return redirect(url_for('pet.pets'))

	except Exception as error:
		return render_template('error.html', message=str(error))


@pet_blueprint.route('/edit', methods=('GET', 'POST',))
def pet_edit():
	id = request.args.get('id')

	if request.method == 'GET':
		pet_type_list = PetTypeBus().get()
		pet_status_list = PetStatusBus().get()

		pet_dict = PetBus().get(id=id)
		return render_template('pet-edit.html', pet_dict=pet_dict[0], pet_type_list=pet_type_list,
		                       pet_status_list=pet_status_list)

	try:
		PetBus().put(id, request.form)
		flash('Successfuly edited Pet', category='message')
		return redirect(url_for('pet.pets'))

	except Exception as error:
		return render_template('error.html', message=str(error))


@pet_blueprint.route('/delete', methods=('POST',))
def pet_delete():
	try:
		PetBus().delete(request.args.get('id'))
		flash('Successfuly deleted Pet', category='message')
		return redirect(url_for('pet.pets'))

	except Exception as error:
		return render_template('error.html', message=str(error))
