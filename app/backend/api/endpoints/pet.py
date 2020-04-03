# coding=utf-8

from flask_restplus import Resource

from app.backend.api.restplus import api
from app.backend.api.serializers.pet import pet_get_serializer, pet_post_serializer
from app.backend.web.business.pet import PetBus

ns_pet = api.namespace('pet', description='Pets operations and registry')


@ns_pet.route('/')
class Pets(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(Pets, self).__init__(api, *args, **kwargs)
		self.bus = PetBus()

	@api.marshal_with(pet_get_serializer)
	def get(self):
		return self.bus.get()

	@api.expect(pet_post_serializer)
	@api.marshal_with(pet_get_serializer, code=201)
	def post(self):
		return self.bus.add(api.payload)


@ns_pet.route('/<int:id>', methods=('GET', 'POST', 'PUT', 'DELETE'))
class Pet(Resource):
	def __init__(self, api=None, *args, **kwargs):
		super(Pet, self).__init__(api, *args, **kwargs)
		self.bus = PetBus()

	@api.marshal_with(pet_get_serializer)
	def get(self, id):
		return self.bus.get(id=id)

	@api.expect(pet_post_serializer)
	@api.marshal_with(pet_get_serializer)
	def put(self, id):
		return self.bus.put(id=id, payload=api.payload)

	def delete(self, id):
		return self.bus.delete(id=id)
