# coding=utf-8

from datetime import datetime

from flask_security import RoleMixin
from flask_sqlalchemy import event

from app.backend.database import db

user_role_table = db.Table(
	'user_role',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)


class Role(db.Model, RoleMixin):
	__tablename__ = 'role'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer(), primary_key=True)

	# String
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))

	# Text
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), default=datetime.utcnow())
	date_modified = db.Column(db.DateTime(), onupdate=datetime.utcnow())
	date_deleted = db.Column(db.DateTime())


# Event Listeners
@event.listens_for(Role.is_deleted, 'set')
def on_changed_is_deleted(target, value, oldvalue, initiator):
	""" Listen for is_deleted changes and update date_deleted """

	target.date_deleted = None
	# If is deleting
	if oldvalue == False and value == True:
		target.is_active = False
		target.date_deleted = datetime.utcnow()
