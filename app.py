from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

mqtt = Mqtt(app)

socketio = SocketIO(app)

from route import *
    
if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, debug=True)
	#app.run('0.0.0.0')
