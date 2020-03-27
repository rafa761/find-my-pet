# coding=utf-8

# Fix error "ImportError: cannot import name 'cached_property' from 'werkzeug'"
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

from app.backend.database import db
from app.config import config_dict


def create_app(config_name=None):
	if not config_name:
		config_name = 'default'

	app = Flask(__name__)
	app.config.from_object(config_dict[config_name])
	config_dict[config_name].init_app(app)

	## Start the modules on app context
	db.init_app(app)

	## Register the BLueprints
	# API RESTful
	from app.backend.api import api_blueprint
	app.register_blueprint(api_blueprint)

	return app
