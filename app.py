#import eventlet
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

#eventlet.monkey_patch()

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

from route import *
    
if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', debug=True, port=5000, use_reloader=True)	# port=5000, use_reloader=True
	#app.run('0.0.0.0')
