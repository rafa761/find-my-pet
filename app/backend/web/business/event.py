# coding=utf-8

from flask_security import current_user

from app.backend.database import db
from app.backend.database.models.event import Event
from app.backend.database.models.pet import Pet
from app.backend.database.models.pet_status import PetStatus


class EventBus(object):
	def add(self, payload):
		event = Event(**payload)

		db.session.add(event)
		db.session.commit()

		return event

	def put(self, id, payload):
		event_list = self.get(id=id)
		if not event_list:
			return

		event_dict = event_list[0]

		for field in event_dict.get_self_attributes(attr_filter=payload.keys()):
			setattr(event_dict, field, payload.get(field))

		db.session.add(event_dict)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		event_list = self.get(id=id)
		if not event_list:
			return

		event_dict = event_list[0]

		try:
			event_dict.is_deleted = True

			db.session.add(event_dict)
			db.session.commit()

		except:
			db.session.rollback()
			return False

		return True

	def get(self, **kwargs):
		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		base_query = db.session.query(Event.id, Event.description, Event.is_deleted, Event.event_date,
		                              Pet.id, Pet.name, PetStatus.description)

		filter_query = base_query.outerjoin(Pet, Event.pet_id == Pet.id).join(PetStatus, Pet.status_id == PetStatus.id)

		if kwargs:
			final_query = filter_query.filter_by(**kwargs).all()

		else:
			final_query = filter_query.all()

		result_list = []
		for record in final_query:
			result_list.append({
				'id': record[0],
				'description': record[1],
				'is_deleted': record[2],
				'event_date': record[3],
				'pet_id': record[4],
				'pet_name': record[5],
				'pet_status_description': record[6],
			})

		return result_list

	def get_all(self, **kwargs):

		if not current_user.is_admin:
			kwargs['is_deleted'] = False

		if len(kwargs) > 0:
			event_list = db.session.query(Event, Pet).join(Pet)
