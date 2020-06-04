# coding=utf-8

from flask import render_template, redirect, url_for, request
from flask_security import current_user

from app.backend.web.business.event import EventBus
from app.backend.web.business.pet import PetBus
from app.frontend.views import event_blueprint


@event_blueprint.route('/events')
def events():
	event_list = EventBus().get()

	return render_template('events.html', event_list=event_list, current_user=current_user)
