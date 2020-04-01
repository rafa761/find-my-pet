# coding=utf-8

from datetime import datetime

from app.backend.database import db


class Pet(db.Model):
	# Definition
	__tablename__ = 'pet'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)
	status_id = db.Column(db.Integer, db.ForeignKey('pet_status.id'))
	type_id = db.Column(db.Integer, db.ForeignKey('pet_type.id'))

	# Float
	weight = db.Column(db.Float(precision=3))

	# String
	name = db.Column(db.String(60), index=True)
	color = db.Column(db.String(30))  # TODO: create other table with colors
	breed = db.Column(db.String(30))  # TODO: create other table with breeds ??

	# Text
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())
	date_deleted = db.Column(db.DateTime())

# Relationship

## Triggers
# TODO: create on change to update date_modified when any field updated.
# TODO: create on change is_deleted to update the date_deleted to uctnow
