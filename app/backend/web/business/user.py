# coding=utf-8

from backend.database import db
from backend.database.models.user import User


class UserBus(object):
	def save(self, payload):
		user = User(**payload)

		db.session.add(user)
		db.session.commit()

		return user

	def delete(self, username):
		user = User.query.filter_by(username=username)

		db.session.remove(user)
		db.session.commit()

		return True

	def get(self, **kwargs):
		if len(kwargs) > 0:
			return User.query.filter_by(**kwargs).first()

		# if do not received any filter params
		return User.query.all()
