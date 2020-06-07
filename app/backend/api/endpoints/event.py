# coding=utf-8

from flask_restplus import Resource

from app.backend.api.restplus import api
from app.backend.api.serializers.event import event_get_serializer, event_post_serializer
from app.backend.web.business.event import EventBus

ns_event = api.namespace('event', description='Events ocurrence')


@ns_event.route('/')
class Events(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(Events, self).__init__(api, *args, **kwargs)
		self.bus = EventBus()

	@api.marshal_with(event_get_serializer)
	def get(self):
		return self.bus.get()

	@api.expect(event_post_serializer)
	@api.marshal_with(event_get_serializer, code=201)
	def post(self):
		return self.bus.add(api.payload)


@ns_event.route('/<int:id>', methods=('GET', 'POST', 'PUT', 'DELETE'))
class Event(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(Event, self).__init__(api, *args, **kwargs)
		self.bus = EventBus()

	@api.marshal_with(event_get_serializer)
	def get(self, id):
		return self.bus.get(id=id)

	@api.expect(event_post_serializer)
	@api.marshal_with(event_get_serializer)
	def put(self, id):
		return self.bus.put(id=id, payload=api.payload)

	def delete(self, id):
		return self.bus.delete(id=id)
