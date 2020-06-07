# coding=utf-8

from datetime import datetime

from flask_sqlalchemy import event

from app.backend.database import db
from app.backend.database.models.base import Base


class Event(db.Model, Base):
	__tablename__ = 'event'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)
	pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), index=True)

	# Text
	description = db.Column(db.Text(), nullable=False)

	# Boolean
	is_deleted = db.Column(db.Boolean(), default=False)

	# DataTime
	event_date = db.Column(db.Date())
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime(), default=datetime.utcnow())
	date_deleted = db.Column(db.DateTime())


# Event Listeners
@event.listens_for(Event.is_deleted, 'set')
def on_change_is_deleted(target, value, oldvalue, initiator):
	""" Listen for is_deleted changes and update date_deleted """

	target.date_deleted = None
	# If is deleting
	if oldvalue is False and value is True:
		target.date_deleted = datetime.utcnow()


@event.listens_for(Event.description, 'set')
def on_change_description(target, value, oldvalue, initiator):
	target.date_modified = None
	if oldvalue != value:
		target.date_modified = datetime.utcnow()
