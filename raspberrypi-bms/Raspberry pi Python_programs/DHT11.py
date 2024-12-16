import time
import sys
import Adafruit_DHT as dht
# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2
while True:
    humidity,temperature = dht.read_retry(dht.DHT11, 4)
    if humidity is not None and temperature is not None:
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print(temperature)        
    else:
        print "Failed to get reading. Try again!"
    time.sleep(INTERVAL)
