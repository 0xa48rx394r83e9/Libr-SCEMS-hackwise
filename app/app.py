from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

from .main import *

app.register_blueprint(main, url_prefix='/main')

if __name__ == '__main__':
    socketio.run(app)