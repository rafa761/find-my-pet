# coding=utf-8

from datetime import datetime

from flask_security import UserMixin
from flask_sqlalchemy import event
from werkzeug.security import generate_password_hash, check_password_hash

from app.backend.database import db
from app.backend.database.models.base import Base
from app.backend.database.models.role import user_role_table, Role


class User(UserMixin, db.Model, Base):
	## Definition
	__tablename__ = 'user'
	__table_args__ = {'extend_existing': True}

	# Integer
	id = db.Column(db.Integer, primary_key=True)

	# String
	username = db.Column(db.String(60), unique=True, index=True, nullable=False)
	password_hash = db.Column(db.String(128))
	email = db.Column(db.String(60), unique=True, index=True, nullable=False)
	first_name = db.Column(db.String(60))
	last_name = db.Column(db.String(60))

	# Text
	info = db.Column(db.Text())

	# Boolean
	is_active = db.Column(db.Boolean(), default=True)
	is_admin = db.Column(db.Boolean(), default=False)
	is_deleted = db.Column(db.Boolean(), default=False)

	# DateTime
	date_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
	date_modified = db.Column(db.DateTime(), onupdate=datetime.utcnow())
	date_deleted = db.Column(db.DateTime())
	date_confirmed = db.Column(db.DateTime())

	# Relationship
	roles = db.relationship(
		Role, secondary=user_role_table, backref=db.backref('user', lazy='dynamic')
	)

	## Properties
	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute!')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	## Several Methods
	def verify_password(self, password):
		""" Check if the received password is correct """
		return check_password_hash(self.password_hash, password)

	## Magic Methods Override
	def __repr__(self):
		return f'<id {self.id}, username {self.username}>'


# Event Listeners
@event.listens_for(User.is_deleted, 'set')
def on_changed_is_deleted(target, value, oldvalue, initiator):
	""" Listen for is_deleted changes and update date_deleted """

	target.date_deleted = None
	# If is deleting
	if oldvalue == False and value == True:
		target.is_active = False
		target.date_deleted = datetime.utcnow()
