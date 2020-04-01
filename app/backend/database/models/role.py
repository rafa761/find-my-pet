# coding=utf-8

from datetime import datetime

from flask_security import RoleMixin

from app.backend.database import db

user_role_table = db.Table(
	'user_role',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)


class Role(db.Model, RoleMixin):
	__tablename__ = 'role'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer(), primary_key=True)

	# String
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())

	## Triggers
	# TODO: create on change to update date_modified when any field updated.
