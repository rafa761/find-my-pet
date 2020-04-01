# coding=utf-8

from flask_restplus import fields

from app.backend.api.restplus import api
from app.backend.api.serializers import custom_fields

user_base_serializer = {
	# Integer
	'id': fields.Integer(required=False, description='User unique ID'),

	# String
	'username': fields.String(required=True, description='Username'),
	'password': fields.String(required=True, description='Password'),
	'first_name': fields.String(required=True, description='First Name'),
	'last_name': fields.String(required=True, description='Last Name'),

	# Text
	'info': fields.String(required=False, description='Free text field'),

	# Custom
	'email': custom_fields.Email(required=True, description='Email address'),

	# Boolean
	'is_active': fields.Boolean(description='Is Active'),
	'is_admin': fields.Boolean(description='Is Administrator'),
	'is_deleted': fields.Boolean(description='Is Deleted'),

	# DateTime
	'date_created': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified'),
	'date_deleted': fields.DateTime(description='Date Deleted')
}

user_get_serializer = api.model('UserGet', {**user_base_serializer})

# user_get_serializer = api.model('UserGet', {
# 	'id': user_base_serializer['id'],
# 	'username': user_base_serializer['username'],
# 	'email': user_base_serializer['email'],
# 	'first_name': user_base_serializer['first_name'],
# 	'last_name': user_base_serializer['last_name'],
# 	'info': user_base_serializer['info'],
# 	'is_active': user_base_serializer['is_active'],
# 	'is_admin': user_base_serializer['is_admin'],
# 	'is_deleted': user_base_serializer['is_deleted'],
# 	'date_created': user_base_serializer['date_created'],
# 	'date_modified': user_base_serializer['date_modified'],
# 	'date_deleted': user_base_serializer['date_deleted']
# })

user_post_serializer = api.model('UserPost', {
	'username': user_base_serializer['username'],
	'password': user_base_serializer['password'],
	'email': user_base_serializer['email'],
	'first_name': user_base_serializer['first_name'],
	'last_name': user_base_serializer['last_name'],
	'info': user_base_serializer['info'],
})
