# coding=utf-8

from datetime import datetime

from backend.database import db


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, index=True)
	# password
	email = db.Column(db.String(60), unique=True, index=True)
	first_name = db.Column(db.String(30))
	last_name = db.Column(db.String(60))
	date_added = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())

	# TODO: create on change to update date_modified when any field updated.

	def __repr__(self):
		return f'<id {self.id}>'
