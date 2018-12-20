import os

DEBUG = True
SECRET_KEY = 'a1b2c3'
STATIC_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')
CACHE_TYPE = "null"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:unlock@localhost:5432/chat_server'
MQTT_BROKER_URL = 'iot.eclipse.org' #'broker.hivemq.com'
MQTT_BROKER_PORT = 1883
#MQTT_CLIENT_ID = 'flask_mqtt'
MQTT_USERNAME = ''
MQTT_PASSWORD = ''
MQTT_KEEPALIVE = 5
MQTT_TLS_ENABLED = False
TEMPLATES_AUTO_RELOAD = True
#MQTT_LAST_WILL_TOPIC = 'chat/#'
#MQTT_LAST_WILL_MESSAGE = ''
#MQTT_LAST_WILL_QOS = 2
#MQTT_REFRESH_TIME = 1.0
