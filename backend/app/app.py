# coding=utf-8

import os

import click
from flask_migrate import Migrate, upgrade
from backend.app.database.db import db
from backend.app import create_app
from backend.app.database.models.user import User

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
	""" Create the shell context, add new models and they will be available in Command line """
	return dict(db=db, User=User)


if __name__ == '__main__':
	db.create_all()
	app.run(host='0.0.0.0', port=7000)
