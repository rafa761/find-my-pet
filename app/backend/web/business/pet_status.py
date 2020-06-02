# coding=utf-8

from flask_security import current_user
from app.backend.database import db
from app.backend.database.models.pet_status import PetStatus


class PetStatusBus(object):
	def add(self, payload):
		pet_status = PetStatus(**payload)

		# Add to the database
		db.session.add(pet_status)
		db.session.commit()

		return pet_status

	def put(self, id, payload):
		# Get from database
		pet_status = self.get(id=id)
		if not pet_status:
			return

		# update the object with incomming payload
		for field in pet_status.get_self_attributes(attr_filter=payload.keys()):
			setattr(pet_status, field, payload.get(field))

		# Add to the database
		db.session.add(pet_status)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		# Get from database
		pet_status = self.get(id=id)
		if not pet_status:
			return

		try:
			# When deleting, we don't delete from the database, but just set as deleted
			pet_status.is_deleted = True

			# Add to the database
			db.session.add(pet_status)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):

		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		if len(kwargs) > 0:
			return PetStatus.query.filter_by(**kwargs).all()

		# if do not received any filter parameter
		return PetStatus.query.all()
