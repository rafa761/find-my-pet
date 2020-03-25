# coding=utf-8

from flask import Flask

from backend.database import db
from config import config_dict


def create_app(config_name=None):
	if not config_name:
		config_name = 'default'

	app = Flask(__name__)
	app.config.from_object(config_dict[config_name])
	config_dict[config_name].init_app(app)

	db.init_app(app)

	return app
