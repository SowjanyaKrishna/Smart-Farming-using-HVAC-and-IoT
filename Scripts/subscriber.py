import paho.mqtt.client as paho
import time
import sys
import datetime
import time

#broker = "localhost"  # host name
#topic = "indoor"  # topic name
MQTT_SERVER = "192.168.0.100"
MQTT_PATH = "indoor_farm"

def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))  # printing Received message
    print("")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)

client = paho.Client()  # create client object

client.on_connect = on_connect
client.on_message = on_message
print("connecting to broker host")
client.connect(MQTT_SERVER,1883,60)  # connection establishment with broker
print("subscribing begins here")
client.subscribe(MQTT_PATH)  # subscribe topic test

while 1:
    client.loop_forever()  # contineously checking for message