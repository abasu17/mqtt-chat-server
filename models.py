from app import *

# Create database model
class Users(db.Model):
	__tablename__ = 'sys_users'
	u_id = db.Column(db.String(32), primary_key=True)
	f_name = db.Column(db.String(25))
	l_name = db.Column(db.String(25))
	mobile_no = db.Column(db.String(10))
	u_name = db.Column(db.String(25))
	password = db.Column(db.String(64))
	signature = db.Column(db.String(64))
	
	def __init__(self, u_id, f_name, l_name, mobile_no, u_name, password, topic):
		self.u_id = u_id
		self.f_name = f_name
		self.l_name = l_name
		self.mobile_no = mobile_no
		self.u_name = u_name
		self.password = password
		self.signature = topic

	def __repr__(self):
		return str(str(self.u_name) + "," + str(self.signature) + "," + str(self.u_id))
	
class Messages(db.Model):
	__tablename__ = 'sys_messages'
	msg_id = db.Column(db.String(32), primary_key=True)
	msg_from = db.Column(db.String(32))	
	msg_to = db.Column(db.String(32))
	msg_body = db.Column(db.String(200))
	msg_timestamp = db.Column(db.String(32))
	
	def __init__(self, msg_id, msg_from, msg_to, msg_body, msg_timestamp):
		self.msg_id = msg_id
		self.msg_from = msg_from
		self.msg_to = msg_to
		self.msg_body = msg_body
		self.msg_timestamp = msg_timestamp

	def __repr__(self):
		return str(self.msg_to)
