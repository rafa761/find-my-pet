# coding=utf-8

import os

from flask_migrate import Migrate

from backend.database import db
from backend.database.models.user import User
from backend.web import create_app

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
	""" Create the shell context, add new models and they will be available in Command line """
	return dict(db=db, User=User)


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(host='0.0.0.0', port=7000)
