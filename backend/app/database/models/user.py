# coding=utf-8

from datetime import datetime
from backend.app.config import GLOBAL_DATETIME_FORMAT
from backend.app.database.db import db


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True, index=True)
	email = db.Column(db.String(60), unique=True, index=True)
	first_name = db.Column(db.String(30))
	last_name = db.Column(db.String(60))
	# password
	date_added = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime())

	# TODO: create on change to update date_modified when any field updated.

	def __repr__(self):
		return f'<id {self.id}>'
