# coding=utf-8

from flask_security import current_user
from app.backend.database import db
from app.backend.database.models.pet import Pet
from app.backend.database.models.pet_status import PetStatus
from app.backend.database.models.pet_type import PetType


class PetBus(object):
	def add(self, payload):
		pet = Pet(**payload)

		db.session.add(pet)
		db.session.commit()

		return pet

	def put(self, id, payload):
		# Get from database
		pet_list = self.get(id=id)
		if not pet_list:
			return

		pet_dict = pet_list[0]

		# Update pet object with incoming payload
		for field in pet_dict.get_self_attributes(attr_filter=payload.keys()):
			setattr(pet_dict, field, payload.get(field))

		# Add to the database
		db.session.add(pet_dict)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		pet_list = self.get(id=id)
		if not pet_list:
			return False

		pet_dict = pet_list[0]

		# When deleting, we don't delete from the database, but just set as deleted
		try:
			pet_dict.is_deleted = True

			# Add to the database
			db.session.add(pet_dict)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):

		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		if len(kwargs) > 0:
			return Pet.query.filter_by(**kwargs).first()

		return Pet.query.all()

	def get_all(self, **kwargs):

		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		if len(kwargs) > 0:
			pet_list = db.session.query(
				Pet,
				PetStatus,
				PetType
			).filter(Pet.status_id == PetStatus.id, Pet.type_id == PetType.id).filter_by(**kwargs).all()
			return pet_list

		pets_list = db.session.query(
			Pet,
			PetStatus,
			PetType
		).filter(Pet.status_id == PetStatus.id, Pet.type_id == PetType.id).all()

		# if do not received any filter parameter
		return pets_list
