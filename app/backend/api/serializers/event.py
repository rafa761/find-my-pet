# coding=utf-8

from flask_restplus import fields

from app.backend.api.restplus import api

event_base_serializer = {
	# Integer
	'id': fields.Integer(required=False, description='Event unique ID'),
	'pet_id': fields.Integer(required=False, description='Pet ID'),

	# Text
	'description': fields.String(required=True, description='Event occurrence description'),

	# Boolean
	'is_deleted': fields.Boolean(description='Is Deleted'),

	# DataTime
	'event_date': fields.DateTime(description='Date of occurrence'),
	'date_created': fields.DateTime(description='Date Created'),
	'date_modified': fields.DateTime(description='Date Modified'),
	'date_deleted': fields.DateTime(description='Date Deleted')
}

event_get_serializer = api.model('EventGet', {**event_base_serializer})

event_post_serializer = api.model('EventPost', {
	'description': event_base_serializer['description'],
	'event_date': event_base_serializer['event_date'],
	'is_deleted': event_base_serializer['is_deleted'],
})
