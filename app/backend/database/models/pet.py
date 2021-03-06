# coding=utf-8

from datetime import datetime

from flask_sqlalchemy import event

from app.backend.database import db
from app.backend.database.models.base import Base


class Pet(db.Model, Base):
	__tablename__ = 'pet'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)
	status_id = db.Column(db.Integer, db.ForeignKey('pet_status.id'))
	type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'))

	# Float
	weight = db.Column(db.Float(precision=3))

	# String
	name = db.Column(db.String(60))
	color = db.Column(db.String(30))  # TODO: create other table with colors
	breed = db.Column(db.String(30))  # TODO: create other table with breeds ??

	# Text
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime(), onupdate=datetime.utcnow())
	date_deleted = db.Column(db.DateTime())

# Relationship


# Event Listeners
@event.listens_for(Pet.is_deleted, 'set')
def on_changed_is_deleted(target, value, oldvalue, initiator):
	""" Listen for is_deleted changes and update date_deleted """

	target.date_deleted = None
	# If is deleting
	if oldvalue is False and value is True:
		target.is_active = False
		target.date_deleted = datetime.utcnow()


@event.listens_for(Pet.info, 'set')
def on_changed_info(target, value, oldvalue, initiator):

	target.date_modified = None
	if oldvalue != value:
		target.date_modified = datetime.utcnow()
