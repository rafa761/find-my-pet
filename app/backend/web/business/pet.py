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
		pet_obj = Pet().query.filter_by(id=id).first()
		if not pet_obj:
			return

		# Update pet object with incoming payload
		for field in pet_obj.get_columns(filter_list=[x for x in payload.keys()]):
			setattr(pet_obj, field, payload[field])

		db.session.add(pet_obj)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		pet_obj = Pet().query.filter_by(id=id).first()
		if not pet_obj:
			return

		# When deleting, we don't delete from the database, but just set as deleted
		try:
			pet_obj.is_deleted = True

			# Add to the database
			db.session.add(pet_obj)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):
		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		base_query = db.session.query(Pet.id, Pet.name, Pet.status_id, Pet.type_id, Pet.weight, Pet.name, Pet.color,
		                              Pet.breed, Pet.info, Pet.is_active, Pet.is_deleted, PetStatus.description,
		                              PetType.description)

		if kwargs:
			base_query = base_query.filter_by(**kwargs)

		join_query = base_query.join(PetStatus, Pet.status_id == PetStatus.id).join(PetType, Pet.type_id == PetType.id)

		order_query = join_query.order_by(Pet.date_modified.desc())

		final_query = order_query.all()

		return [{
				'id': record[0],
				'name': record[1],
				'status_id': record[2],
				'type_id': record[3],
				'weight': record[4],
				'name': record[5],
				'color': record[6],
				'breed': record[7],
				'info': record[8],
				'is_active': record[9],
				'is_deleted': record[10],
				'status_description': record[11],
				'type_description': record[12],
			} for record in final_query]
