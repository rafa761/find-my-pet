# coding=utf-8

from flask_restplus import Api

api = Api(
	version='1.0',
	title='Find My Pet',
	description='The tool to find your beloved friend'
)


@api.errorhandler
def default_error_handler(e):
	message = 'Unexpected error occurred!'
	return {'message': message}, 500
