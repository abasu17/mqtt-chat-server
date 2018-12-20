from app import *
from datetime import timedelta
from flask import render_template, request, session, send_from_directory, redirect, url_for
import os, time
from plugins import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_
from models import *
import json


@app.route('/', methods=['GET', 'POST'])
def user_login():
	error_check = 0
	session['auth'] = False
	u_id = None
	password = None
	
	if request.method == 'POST':
		u_id = request.form['inputUserID']
		passwd = encrypt_string(request.form['inputPassword'])
		check_registered_user = db.session.query(Users).filter(or_(Users.u_name == u_id, Users.mobile_no == u_id), Users.password == passwd).first()
		if check_registered_user is None:
			error_check = 1
		else:
			new_data = str(check_registered_user).split(',')
			session['auth'] = True
			session['user_name'] = new_data[0]
			session['signature'] = new_data[1]
			session['u_id'] = new_data[2]
			return redirect( url_for('chatting') ) 

	return render_template('user_login/user_login.html', err_chk = error_check)


@app.route('/user_registration', methods=['GET', 'POST'])
def user_registration():
	error_check = 0
	u_id = None
	f_name = None
	l_name = None
	mobile_no = None
	u_name = None
	password = None
	signature = None
	
	if request.method == 'POST':
		
		if (request.form['inputPassword'] == request.form['inputConfPassword']):
			u_id = uuid()
			f_name = request.form['inputFname']
			l_name = request.form['inputLname']
			mobile_no = request.form['inputMobile']
			u_name = request.form['inputUserName']
			password = encrypt_string(request.form['inputPassword'])
			signature = encrypt_string(str(u_name) + str(mobile_no))
			
			if not db.session.query(Users).filter(Users.u_name == u_name).count() and not db.session.query(Users).filter(Users.mobile_no == mobile_no).count():
				reg = Users(u_id, f_name, l_name, mobile_no, u_name, password, signature)
				db.session.add(reg)
				db.session.commit()
				return redirect('/')
			else:
				error_check = 1

	return render_template('user_registration/user_registration.html',  err_chk = error_check)

@app.route('/chatting', methods=['GET', 'POST'])
def chatting():
	if (not session['auth']):
		return redirect('/')
	get_users = db.session.query(Users).with_entities(Users.f_name, Users.l_name, Users.u_id, Users.u_name, Users.signature)
	return render_template('sys_chatbox/sys_chatbox.html', users = list(get_users), curr_user = session['user_name'], curr_sign = session['signature'])

@app.route('/store_msg', methods=['GET', 'POST'] )
def store_msg():
	if (not session['auth']):
		return redirect('/')

	if (request.form['selectUser'] != None and request.form['inputMsgBox'] != None):
		msg_id = uuid()
		msg_from = db.session.query(Users).with_entities(Users.u_id).filter(Users.u_name == session['user_name'])
		msg_to = request.form['selectUser']
		msg_body = request.form['inputMsgBox']
		msg_timestamp = get_time()

		msg_store = Messages(msg_id, msg_from, msg_to, msg_body, msg_timestamp)
		db.session.add(msg_store)
		db.session.commit()
		return "Data stored."

@app.route('/get_record', methods=['GET', 'POST'])
def get_record():
	if (not session['auth']):
		return redirect('/')

	get_msg = db.session.query(Messages.msg_timestamp, '|'+Users.u_name, Messages.msg_body).outerjoin(Users, Users.u_id == Messages.msg_from).filter(or_(and_(Messages.msg_from == str(request.form['data_id']), Messages.msg_to == session['u_id']), and_(Messages.msg_from == session['u_id'], Messages.msg_to == str(request.form['data_id'])))).limit(100).all()
	return str(get_msg).replace("[", "").replace("('", "[").replace("')," , '&#13;').replace("',)", "").replace("]", "").replace("', '", "] : ").replace("')", "").replace("] : |", " @ ")

@app.route('/get_time_now', methods=['GET', 'POST'] )
def get_time_now():
	return get_time()

@app.route('/logout')
def logout():
	mqtt.unsubscribe_all()
	session.pop('auth')
	session.pop('user_name')
	return redirect('/')

''' SocketIO Setup '''
@socketio.on('publish')
def handle_publish(json_str):
	print("\n\n Data published!!!\n")
	data = json.loads(json_str)
	print(data)
	mqtt.publish(data['topic'], data['message'], data['qos'])
	print("\n\n")

@socketio.on('subscribe')
def handle_subscribe(json_str):
	print("\n\n Data subscribed!!!\n")
	data = json.loads(json_str)
	print(data)
	mqtt.subscribe(data['topic'], data['qos'])
	print("\n\n")
	
''' MQTT Callbacks '''
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
	mqtt.subscribe('chat/#')
	print("Connected!")

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
	print("\n\n On Message!!!\n")
	data = dict( topic=message.topic, payload=message.payload.decode(), qos=message.qos, time=get_time())
	print(data)
	socketio.emit('mqtt_message', data=data)
	print("\n\n")

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    if level == MQTT_LOG_ERR:
        print('Error: {}'.format(buf))
