# coding=utf-8

from flask_restplus import fields

from backend.api.restplus import api

user_base_serializer = {
	'id': fields.String(required=False, description='User unique ID'),
	'username': fields.String(required=True, description='Username'),
	# 'password'
	'email': fields.String(required=True, description='Email address'),
	'first_name': fields.String(required=True, description='First Name'),
	'last_name': fields.String(required=True, description='Last Name'),
	'date_added': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified')
}

user_get_serializer = api.model('UserGet', {
	'username': user_base_serializer['username'],
	'email': user_base_serializer['email'],
	'first_name': user_base_serializer['first_name'],
	'last_name': user_base_serializer['last_name'],
	'date_added': user_base_serializer['date_added']
})

user_post_serializer = api.model('UserPost', {
	'username': user_base_serializer['username'],
	# password
	'email': user_base_serializer['email'],
	'first_name': user_base_serializer['first_name'],
	'last_name': user_base_serializer['last_name']
})

user_response_serializer = api.model('UserResponse', {
	'id': user_base_serializer['id'],
	'username': user_base_serializer['username'],
	'date_added': user_base_serializer['date_added']
})
