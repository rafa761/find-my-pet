# coding=utf-8

from app.backend.database import db
from app.backend.database.models.user import User


class UserBus(object):
	def add(self, payload):
		user = User(**payload)

		db.session.add(user)
		db.session.commit()

		return user

	def delete(self, username):
		user = User.query.filter_by(username=username).first()

		# When a user is deleted, we don't delete from the database, but just set as deleted
		try:
			user.is_active = False
			user.is_deleted = True
			db.session.add(user)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):
		if len(kwargs) > 0:
			return User.query.filter_by(**kwargs).first()

		# if do not received any filter parameter
		return User.query.all()
