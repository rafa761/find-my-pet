# coding=utf-8

from flask_restplus import Resource

from app.backend.api.restplus import api
from app.backend.api.serializers.pet_status import pet_status_get_serializer, pet_status_post_serializer
from app.backend.web.business.pet_status import PetStatusBus

ns_pet_status = api.namespace('pet_status', description='Status situations for the pets')


@ns_pet_status.route('/')
class PetStatuses(Resource):
	def __init__(self, app=None, *args, **kwargs):
		super(PetStatuses, self).__init__(app, *args, **kwargs)
		self.bus = PetStatusBus()

	@api.marshal_with(pet_status_get_serializer)
	def get(self):
		return self.bus.get()

	@api.expect(pet_status_post_serializer)
	@api.marshal_with(pet_status_get_serializer)
	def post(self):
		return self.bus.add(api.payload)


@ns_pet_status.route('/<int:id>', methods=('GET', 'POST', 'PUT', 'DELETE'))
class PetStatus(Resource):
	def __init__(self, app=None, *args, **kwargs):
		super(PetStatus, self).__init__(app, *args, **kwargs)
		self.bus = PetStatusBus()

	@api.marshal_with(pet_status_get_serializer)
	def get(self, id):
		return self.bus.get(id=id)

	@api.expect(pet_status_post_serializer)
	@api.marshal_with(pet_status_get_serializer)
	def put(self, id):
		return self.bus.put(id=id, payload=api.payload)

	def delete(self, id):
		return self.bus.delete(id=id)
