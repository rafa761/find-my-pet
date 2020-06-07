# coding=utf-8

from datetime import datetime
from dateutil.parser import parse
from flask_security import current_user

from app.backend.database import db
from app.backend.database.models.event import Event
from app.backend.database.models.pet import Pet
from app.backend.database.models.pet_status import PetStatus


class EventBus(object):
	def add(self, payload):

		event = Event(**payload)

		if event.event_date:
			event.event_date = datetime.strptime(event.event_date, '%Y-%m-%d')

		db.session.add(event)
		db.session.commit()

		return event

	def put(self, id, payload):
		event_obj = Event().query.filter_by(id=id).first()
		if not event_obj:
			return

		for field in event_obj.get_columns(filter_list=[x for x in payload.keys()]):
			setattr(event_obj, field, payload[field])

		# Date correction
		if event_obj.event_date:
			event_obj.event_date = parse(event_obj.event_date)

		db.session.add(event_obj)
		db.session.commit()

		return self.get(id=id)

	def delete(self, id):
		event_obj = Event().query.filter_by(id=id).first()
		if not event_obj:
			return

		try:
			event_obj.is_deleted = True

			db.session.add(event_obj)
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

		if kwargs:
			base_query = base_query.filter_by(**kwargs)

		join_query = base_query.outerjoin(Pet, Event.pet_id == Pet.id).outerjoin(PetStatus, Pet.status_id == PetStatus.id)

		order_query = join_query.order_by(Event.event_date.desc())

		final_query = order_query.all()

		result_list = []
		for record in final_query:
			result_list.append({
				'id': record[0],
				'description': record[1],
				'is_deleted': record[2],
				'event_date': datetime.strftime(record[3], '%d/%m/%Y'),
				'pet_id': record[4] or '',
				'pet_name': record[5] or '',
				'pet_status_description': record[6] or '',
			})

		return result_list
