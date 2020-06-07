# coding=utf-8

from flask import Blueprint

main_blueprint = Blueprint('main', __name__)
pet_blueprint = Blueprint('pet', __name__, url_prefix='/pet')
event_blueprint = Blueprint('event', __name__, url_prefix='/event')

from app.frontend.views import main, pet, event
