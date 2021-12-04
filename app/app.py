from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True)

from .pain import *

app.register_blueprint(pain, url_prefix='/pain')

if __name__ == '__main__':
    socketio.run(app)