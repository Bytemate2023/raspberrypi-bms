import RPi.GPIO as GPIO
import paho.mqtt.client as paho
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  #client.subscribe("topic/test")
 
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    print msg.payload
    if(msg.payload == "ON"):
      GPIO.output(3,GPIO.LOW)
      print ("LED ON")
      
    else:
       GPIO.output(3,GPIO.HIGH)
       print ("LED OFF")
      
      
 

client = paho.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("LED/Netra", qos=0)
client.loop_forever()





