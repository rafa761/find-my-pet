# coding=utf-8

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from backend.database import db


class User(db.Model):
	## Definitions
	__tablename__ = 'users'

	# Integer
	id = db.Column(db.Integer, primary_key=True)

	# String
	username = db.Column(db.String(60), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(60), unique=True, index=True)
	first_name = db.Column(db.String(60))
	last_name = db.Column(db.String(60))

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_admin = db.Column(db.Boolean(), default=False)

	# DateTime
	date_added = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())

	## Properties
	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute!')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	## Triggers
	# TODO: create on change to update date_modified when any field updated.

	## Several Methods
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	## Magic Methods Override
	def __repr__(self):
		return f'<id {self.id}, username {self.username}>'
