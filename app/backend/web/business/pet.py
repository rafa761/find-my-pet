# coding=utf-8

from app.backend.database import db
from app.backend.database.models.pet import Pet


class PetBus(object):
	def add(self, payload):
		pet = Pet(**payload)

		db.session.add(pet)
		db.session.commit()

		return pet

	def delete(self, id):
		pet = Pet.query.filter_by(id=id).first()

		# When a pet is deleted, we don't delete from the database, but just set as deleted
		try:
			pet.is_active = False
			pet.is_deleted = True
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
