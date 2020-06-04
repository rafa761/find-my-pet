# coding=utf-8

from flask_security import current_user
from app.backend.database import db
from app.backend.database.models.pet_type import PetType


class PetTypeBus(object):
	def add(self, payload):
		pet_type = PetType(**payload)

		# Add to the database
		db.session.add(pet_type)
		db.session.commit()

		return pet_type

	def put(self, id, payload):
		# Get from database
		pet_type = self.get(id=id)
		if not pet_type:
			return

		# update the object with incomming payload
		for field in pet_type.get_self_attributes(attr_filter=payload.keys()):
			setattr(pet_type, field, payload.get(field))

		# add to the database
		db.session.add(pet_type)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		pet_type = self.get(id=id)
		if not pet_type:
			return

		try:
			# When deleting, we don't delete from the database, but just set as deleted
			pet_type.is_deleted = True

			db.session.add(pet_type)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):

		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		if len(kwargs) > 0:
			return PetType.query.filter_by(**kwargs).all()

		return PetType.query.all()
