# coding=utf-8

from flask import Blueprint

main = Blueprint('main', __name__)
pet = Blueprint('pet', __name__, url_prefix='/pet')

from app.frontend.main import views, pet_view
