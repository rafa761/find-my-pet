# coding=utf-8

import os
from dateutil.parser import parse

from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.backend.database import db
from app.backend.database.models.pet import Pet
from app.backend.database.models.role import Role
from app.backend.database.models.pet_status import PetStatus
from app.backend.database.models.pet_type import PetType
from app.backend.database.models.user import User
from app.backend.database.models.event import Event
from app.backend.web import create_app
from app.config import MIGRATION_DIR
from flask import render_template

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
migrate = Migrate(app, db, directory=MIGRATION_DIR)
bootstrap = Bootstrap(app)


@app.shell_context_processor
def make_shell_context():
	""" Create the shell context, add new models and they will be available in Command line """
	return dict(
		db=db,
		User=User,
		Role=Role,
		Pet=Pet,
		PetStatus=PetStatus,
		PetType=PetType,
		Event=Event
	)


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
	date = parse(date)
	native = date.replace(tzinfo=None)
	format = '%Y-%m-%d'

	return native.strftime(format)


@app.errorhandler
def default_error_handler(Exception):
	# return {'message': str(error)}, getattr(error, 'code', 500)
	return render_template('error.html'), 500


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000)
