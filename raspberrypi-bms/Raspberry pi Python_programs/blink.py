import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setwarnings(False)
n=0.5
GPIO.setmode(GPIO.BCM)      ## Use board pin numbering
GPIO.setup(17, GPIO.OUT)      ## Setup GPIO Pin 11 to OUT
while True:
	GPIO.output(17,True)  ## Turn on Led
	time.sleep(n)         ## Wait for one second
	GPIO.output(17,False) ## Turn off Led
	time.sleep(n)         ## Wait for one second
