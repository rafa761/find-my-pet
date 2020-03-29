# coding=utf-8

import os

## Constants
GLOBAL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
MIGRATION_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__) , 'backend\database\migrations'))


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
	GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID',
	                                   '46995395977-v6o8uo17vn3skoapndfra198487t9jfd.apps.googleusercontent.com')
	GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET', 'MT1P7CC9CzFcznP-1m3IXKVc')
	OAUTHLIB_RELAX_TOKEN_SCOPE = True
	OAUTHLIB_INSECURE_TRANSPORT = True

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	# Flask
	DEBUG = True

	# Database
	basedir = os.path.dirname(__file__)
	databasedir = os.path.abspath(os.path.join(basedir, 'backend\database'))
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(databasedir, 'fmp-dev.sqlite')}"


class TestingConfig(Config):
	# Flask
	TESTING = True
	DEBUG = True

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
