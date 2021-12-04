from flask import Blueprint

pain = Blueprint('pain', __name__)

from . import views
