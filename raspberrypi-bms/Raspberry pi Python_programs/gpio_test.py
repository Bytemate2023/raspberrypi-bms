import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library for delays

# Pin configuration
BUTTON_PIN = 17  # GPIO 17 (Pin 11 on the Raspberry Pi board)

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering (GPIO 17 = Pin 11)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set as input with pull-down resistor

try:
    while True:
        # Digital read
        button_state = GPIO.input(BUTTON_PIN)
        
        if button_state == GPIO.HIGH:  # Check if button is pressed
            print("Button Pressed!")
        else:
            print("Button Released")
        
        time.sleep(0.1)  # Delay to reduce CPU usage

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    GPIO.cleanup()  # Reset all GPIO pins to a safe state
