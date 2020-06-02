# coding=utf-8

import os

from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.backend.database import db
from app.backend.database.models.pet import Pet
from app.backend.database.models.role import Role
from app.backend.database.models.pet_status import PetStatus
from app.backend.database.models.pet_type import PetType
from app.backend.database.models.user import User
from app.backend.web import create_app
from app.config import MIGRATION_DIR

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
		PetType=PetType
	)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7000)
