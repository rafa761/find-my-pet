# coding=utf-8

from app.backend.database import db
from app.backend.database.models.pet import Pet


class PetBus(object):
	def add(self, payload):
		pet = Pet(**payload)

		db.session.add(pet)
		db.session.commit()

		return pet

	def put(self, id, payload):
		# Get from database
		pet = self.get(id=id)
		if not pet:
			return

		# Update pet object with incoming payload
		for field in pet.get_self_attributes(attr_filter=payload.keys()):
			setattr(pet, field, payload.get(field))

		# Add to the database
		db.session.add(pet)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		pet = self.get(id=id)
		if not pet:
			return False

		# When deleting, we don't delete from the database, but just set as deleted
		try:
			pet.is_deleted = True

			# Add to the database
			db.session.add(pet)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):
		if len(kwargs) > 0:
			return Pet.query.filter_by(**kwargs).first()

		# if do not received any filter parameter
		return Pet.query.all()
