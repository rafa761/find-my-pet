# coding=utf-8

from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Create the database tables
def create_all():
	with current_app.app_context():
		db.create_all()
