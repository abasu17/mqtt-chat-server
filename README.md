# mqtt-chat-server

This project is developed on Python Platform. This is a simple chatting application implemented with MQTT protocol.
- **Python Version** : 3.6+
- **Flask Version** : 1.0.2

## Setup Database Environment
###### Install postgresql-10
> $ **sudo apt-get install postgresql-10**

###### Install postgresql-development environment
> $ **sudo apt-get install postgresql postgresql-contrib libpq-dev**

###### Install pgadmin3
> $ **sudo apt install pgadmin3**

## Setup Python Environment
###### Install SQLAlchemy for ORM
> $ **pip3 install psycopg2 Flask-SQLAlchemy Flask-Migrate SQLAlchemy**

###### Install Flask-MQTT
> $ **pip3 install Flask-MQTT**

###### Install SocketIO
> $ **pip3 install flask-socketio**

###### Install Eventlet
> $ **pip3 install eventlet**

## Setup Project
###### Clone GIT
> $ **git clone https://github.com/abasu17/mqtt-chat-server.git**

###### Setup Database
> - $ **cd mqtt-chat-server**
> - $ **python3**

###### On Pyhton terminal.
> - >> **from app import db**
> - >> **db.create_all()**
> - >> **exit()**
