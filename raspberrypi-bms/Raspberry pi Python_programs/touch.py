import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
Pin = 23
GPIO.setup(Pin, GPIO.IN)
while True:
    Pressed =  GPIO.input(Pin)
    if Pressed == 1 :
        print "PRESSED"
    else:
        print "NOT PRESSED"
    time.sleep(0.1)
