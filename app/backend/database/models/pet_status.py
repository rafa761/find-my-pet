# coding=utf-8

from datetime import datetime

from flask_sqlalchemy import event

from app.backend.database import db
from app.backend.database.models.base import Base


class PetStatus(db.Model, Base):
	# Definition
	__tablename__ = 'pet_status'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)

	# String
	description = db.Column(db.String(60))
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime(), onupdate=datetime.utcnow())
	date_deleted = db.Column(db.DateTime())

	## Magic Methods Override
	def __repr__(self):
		return f'<id {self.id}, description {self.description}>'


# Event Listeners
@event.listens_for(PetStatus.is_deleted, 'set')
def on_changed_is_deleted(target, value, oldvalue, initiator):
	""" Listen for is_deleted changes and update date_deleted """

	target.date_deleted = None
	# If is deleting
	if oldvalue == False and value == True:
		target.is_active = False
		target.date_deleted = datetime.utcnow()


@event.listens_for(PetStatus.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
	db.session.add(PetStatus(description='lost'))
	db.session.add(PetStatus(description='rescued'))
	db.session.add(PetStatus(description='adopted'))
	db.session.add(PetStatus(description='other'))
	db.session.commit()
