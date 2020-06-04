# coding=utf-8

from flask_restplus import fields

from app.backend.api.restplus import api

pet_status_base_serializer = {
	# Integer
	'id': fields.Integer(required=False, description='Pet status unique ID'),

	# String
	'description': fields.String(required=True, description='Status description'),
	'info': fields.String(required=False, description='Free text field'),

	# Boolean
	'is_active': fields.Boolean(description='Is Active'),
	'is_deleted': fields.Boolean(description='Is Deleted'),

	# DateTime
	'date_created': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified'),
	'date_deleted': fields.DateTime(description='Date Deleted')
}

pet_status_get_serializer = api.model('PetStatusGet', {**pet_status_base_serializer})

pet_status_post_serializer = api.model('PetStatusPost', {
	'description': pet_status_base_serializer['description'],
	'info': pet_status_base_serializer['info']
})
