# coding=utf-8

from flask import render_template, redirect, url_for, request, flash
from flask_security import current_user

from app.backend.web.business.event import EventBus
from app.backend.web.business.pet import PetBus
from app.frontend.views import event_blueprint


@event_blueprint.route('/events')
def events():
	event_list = EventBus().get()

	return render_template('events.html', event_list=event_list, current_user=current_user)


@event_blueprint.route('/add', methods=('GET', 'POST',))
def add():
	if request.method == 'GET':
		return render_template('event-add.html')

	try:
		EventBus().add(request.form)
		flash('Successfuly saved Event', category='message')
		return redirect(url_for('event.events'))

	except Exception as error:
		return render_template('error.html', message=str(error))


# @event_blueprint.route('/edit', methods=('GET', 'POST',))
# def edit():
# 	pass
#
#
# @event_blueprint('/delete', methods=('GET', 'POST',))
# def delete():
# 	pass
