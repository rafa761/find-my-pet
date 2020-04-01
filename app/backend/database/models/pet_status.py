# coding=utf-8

from datetime import datetime

from app.backend.database import db


class PetStatus(db.Model):
	# Definition
	__tablename__ = 'pet_status'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)

	# String
	description = db.Column(db.String(60))
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())
	date_deleted = db.Column(db.DateTime())

	# Trigger
	# TODO: Create event to update date_modified and date_deleted
