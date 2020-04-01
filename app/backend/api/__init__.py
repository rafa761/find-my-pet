# coding=utf-8

from flask import Blueprint

from app.backend.api.restplus import api
from app.backend.database import create_all

# importing the namespaces
from app.backend.api.endpoints.user import ns_user
from app.backend.api.endpoints.pet import ns_pet

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api.init_app(api_blueprint)

# add the namespaces
api.add_namespace(ns_user)
api.add_namespace(ns_pet)


# Create database before first request
@api_blueprint.before_app_first_request
def create_db():
	create_all()
