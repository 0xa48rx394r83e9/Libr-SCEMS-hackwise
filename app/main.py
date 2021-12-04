import os

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
