
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  #client.subscribe("topic/test")
 
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
 

client = paho.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("BVB/Netra", qos=0)

client.loop_forever()
