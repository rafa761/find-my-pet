# coding=utf-8

from flask import Blueprint
from app.backend.api.restplus import api

# importing the namespaces
from app.backend.api.endpoints.user import ns_user

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api.init_app(api_blueprint)

# add the namespaces
api.add_namespace(ns_user)
