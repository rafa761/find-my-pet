# coding=utf-8

from app.backend.database import db
from app.backend.database.models.user import User


class UserBus(object):
	def add(self, payload):
		user = User(**payload)

		# Add to the database
		db.session.add(user)
		db.session.commit()

		return user

	def put(self, username, payload):
		# Get from database
		user = self.get(username=username)
		if not user:
			return

		# Update object with incoming payload
		for field in user.get_self_attributes(attr_filter=payload.keys()):
			setattr(user, field, payload.get(field))

		# Add to the database
		db.session.add(user)
		db.session.commit()

		return self.get(username=username)

	def delete(self, username):
		# Get from database
		user = self.get(username=username)
		if not user:
			return False

		try:
			# When deleting, we don't delete from the database, but just set as deleted
			user.is_deleted = True

			# Add to the database
			db.session.add(user)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):
		# Try to find with the received parameters
		if len(kwargs) > 0:
			return User.query.filter_by(**kwargs).first()

		# if do not received any filter parameter
		return User.query.all()
