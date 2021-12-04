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

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@main.route('/classroom')
@login_required
def classroom():
    return render_template('classroom.html', name=current_user.name)

@main.route('/courses')
@login_required
def courses():
    return render_template('courses.html', name=current_user.name)

@main.route('/past_papers')
@login_required
def past_papers():
    return render_template('file-dir.html', name=current_user.name)

@main.route('/projects')
@login_required
def projects():
    return render_template('projects.html', name=current_user.name)

@main.route('/universities') #WIP
@login_required
def universities():
    return render_template('uni.html', name=current_user.name)

# @main.route('/ide') #WIP
# @login_required
# def ide():
#     return render_template('profile.html', name=current_user.name)