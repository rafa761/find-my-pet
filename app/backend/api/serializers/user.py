# coding=utf-8

from flask_restplus import fields

from app.backend.api.restplus import api
from app.backend.api.serializers import custom_fields

user_base_serializer = {
	'id': fields.Integer(required=False, description='User unique ID'),
	'username': fields.String(required=True, description='Username'),
	'password': fields.String(required=True, description='Password'),
	'email': custom_fields.Email(required=True, description='Email address'),
	'first_name': fields.String(required=True, description='First Name'),
	'last_name': fields.String(required=True, description='Last Name'),
	'is_active': fields.Boolean(description='Registry situation status'),
	'is_admin': fields.Boolean(description='Is Administrator'),
	'date_added': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified')
}

user_get_serializer = api.model('UserGet', {
	'id': user_base_serializer['id'],
	'username': user_base_serializer['username'],
	'email': user_base_serializer['email'],
	'first_name': user_base_serializer['first_name'],
	'last_name': user_base_serializer['last_name'],
	'is_active': user_base_serializer['is_active'],
	'is_admin': user_base_serializer['is_admin'],
	'date_added': user_base_serializer['date_added'],
	'date_modified': user_base_serializer['date_modified']
})

user_post_serializer = api.model('UserPost', {
	'username': user_base_serializer['username'],
	'password': user_base_serializer['password'],
	'email': user_base_serializer['email'],
	'first_name': user_base_serializer['first_name'],
	'last_name': user_base_serializer['last_name']
})

user_response_serializer = api.model('UserResponse', {
	'id': user_base_serializer['id'],
	'username': user_base_serializer['username'],
	'is_active': user_base_serializer['is_active'],
	'is_admin': user_base_serializer['is_admin'],
	'date_added': user_base_serializer['date_added'],
	'date_modified': user_base_serializer['date_modified']
})
