import os

from flask import Blueprint, render_template, request, jsonify, Response
from flask_login import login_required, current_user
from camera import Camera
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

@main.route('/mentor') #WIP
@login_required
def mentor():
    return render_template('mentor.html', name=current_user.name)

from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# @main.route('/ide') #WIP
# @login_required
# def ide():
#     return render_template('profile.html', name=current_user.name)