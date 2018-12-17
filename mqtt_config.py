import paho.mqtt.client as mqtt

# callbacks
def on_connect (client, userdata, flags, rc):
	print ("Connected with code : " + str(rc))
	client.subscribe("chat_server/#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

broker =  "iot.eclipse.org"
broker_port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
