# coding=utf-8

from flask_restplus import fields

from app.backend.api.restplus import api
from app.backend.api.serializers import custom_fields

pet_base_serializer = {
	# Integer
	'id': fields.Integer(required=False, description='Pet unique ID'),
	'status_id': fields.Integer(required=False, description='Status ID code'),
	'type_id': fields.Integer(required=False, description='Type ID code'),

	# Float
	'weight': fields.Float(required=False, description='Weight'),

	# String
	'name': fields.String(required=False, description='Name'),
	'color': fields.String(required=False, description='Pet color'),
	'breed': fields.String(required=False, description='Breed'),

	# Text
	'info': fields.String(required=False, description='Free text field'),

	# Boolean
	'is_active': fields.Boolean(description='Is Active'),
	'is_deleted': fields.Boolean(description='Is Deleted'),

	# DateTime
	'date_created': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified'),
	'date_deleted': fields.DateTime(description='Date Deleted')
}

pet_get_serializer = api.model('PetGet', {**pet_base_serializer})

pet_post_serializer = api.model('PetPost', {
	'status_id': pet_base_serializer['status_id'],
	'type_id': pet_base_serializer['type_id'],
	'weight': pet_base_serializer['weight'],
	'name': pet_base_serializer['name'],
	'color': pet_base_serializer['color'],
	'breed': pet_base_serializer['breed'],
	'info': pet_base_serializer['info'],
	'is_deleted': pet_base_serializer['is_deleted'],
})
