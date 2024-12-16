import paho.mqtt.client as paho
import time
import json

def on_connect(client, userdata, rc):
    print("Connection returned result: "+connack_string(rc))
 
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
    print("client: "+str(client))
    print("userdata: "+str(userdata))
    print "Message Published..."
 
ACCESS_TOKEN = 'WHXvTlgKHkfsad4nV00J'

 
client = paho.Client()
client.on_publish = on_publish
client.username_pw_set(ACCESS_TOKEN)
client.connect("demo.thingsboard.io", 1883)
client.loop_start()
 
while True:
    attri={'temp':25}
    #json.dumps(attri)
    (rc, mid) = client.publish("v1/devices/me/attributes", json.dumps(attri), qos=1)
    print rc
    print mid
	#client.publish("",)
    time.sleep(1)
