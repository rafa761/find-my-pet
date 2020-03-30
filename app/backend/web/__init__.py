# coding=utf-8

# Fix error "ImportError: cannot import name 'cached_property' from 'werkzeug'"
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask

from app.backend.database import db
from app.backend.database.models.oauth import security, user_datastore
from app.config import config_dict


def create_app(config_name=None):
	if not config_name:
		config_name = 'default'

	app = Flask(__name__, static_folder='../../frontend/static', template_folder='../../frontend/templates')
	app.config.from_object(config_dict[config_name])
	config_dict[config_name].init_app(app)

	## Start the modules on app context
	db.init_app(app)
	security.init_app(app, user_datastore)

	## Register the BLueprints
	# API RESTful
	from app.backend.api import api_blueprint
	app.register_blueprint(api_blueprint)

	# OAuth and Login
	from backend.web.oauth import oauth_blueprint
	app.register_blueprint(oauth_blueprint, url_prefix='/login')

	# Frontend
	from app.frontend.main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
