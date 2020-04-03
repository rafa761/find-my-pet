# coding=utf-8

import os
from pathlib import Path

## Constants
GLOBAL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
MIGRATION_DIR = Path(__file__).parent.joinpath('backend\database\migrations')


class Config:
	# Flask
	SECRET_KEY = os.getenv('SECRET_KEY', '5swZQ71F1KtT!nJgC&MavSW4AOUeHljKOxKsXW6r0WD86$RrZ$')
	FLASK_ENV = os.getenv('FLASK_ENV', 'development')
	DEBUG = False
	TESTING = False
	RESTPLUS_VALIDATE = True
	ERROR_404_HELP = False
	FLASK_RUN_PORT = int(os.getenv('FLASK_RUN_PORT', 7000))

	# SQLAlchemy
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Database
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

	# Third Party Auth
	# Google Auth
	GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
	GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	# Flask
	DEBUG = True

	# Database
	SQLALCHEMY_ECHO = True  # log all the statements issued to stderr
	SQLALCHEMY_TRACK_MODIFICATIONS = True  # track modifications of objects and emit signals
	databasedir = Path(__file__).parent.joinpath('backend\database')
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(databasedir, 'fmp-dev.sqlite')}"


class TestingConfig(Config):
	# Flask
	TESTING = True
	DEBUG = True

	# Flask Forms
	WTF_CSRF_ENABLED = False

	# Database
	SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(Config):
	# Database
	POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
	POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
	POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
	POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', 5433))  # 5432 is already in use on my machine
	POSTGRES_DB = os.getenv('POSTGRES_DB', 'fmp')
	DEFAULT_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', DEFAULT_DATABASE_URL)


# Dict to instantiate config classes
config_dict = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig
}
