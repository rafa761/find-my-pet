# coding=utf-8

from flask_restplus import Resource

from app.backend.api.restplus import api
from app.backend.api.serializers.user import user_get_serializer, user_post_serializer

from app.backend.web.business.user import UserBus

ns_user = api.namespace('user', description='Users operations and registry')


@ns_user.route('/')
class Users(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(Users, self).__init__(api, *args, **kwargs)
		self.bus = UserBus()

	@api.marshal_with(user_get_serializer)
	def get(self):
		return self.bus.get()

	@api.expect(user_post_serializer)
	@api.marshal_with(user_get_serializer, code=201)
	def post(self):
		return self.bus.add(api.payload)


@ns_user.route('/<username>', methods=('GET', 'POST', 'PUT', 'DELETE'))
class User(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(User, self).__init__(api, *args, **kwargs)
		self.bus = UserBus()

	@api.marshal_with(user_get_serializer)
	def get(self, username):
		return self.bus.get(username=username)

	@api.expect(user_post_serializer)
	@api.marshal_with(user_get_serializer)
	def put(self, username):
		return self.bus.put(username=username, payload=api.payload)

	def delete(self, username):
		return self.bus.delete(username=username)
