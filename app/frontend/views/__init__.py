# coding=utf-8

from flask import Blueprint

main_blueprint = Blueprint('main', __name__)
pet_blueprint = Blueprint('pet', __name__, url_prefix='/pet')

from app.frontend.views import main, pet
