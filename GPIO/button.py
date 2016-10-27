#!/usr/bin/python


# Imports
import RPi.GPIO as GPIO
import time


# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

print('Press the button to turn on the light')

# Turns on the light while the button is pressed
try:
	while True:
		if GPIO.input(26):
			GPIO.output(17, False)
		else:
			GPIO.output(17, True)
	
		time.sleep(0.5)

# Cleanup	
except KeyboardInterrupt:
	print("\nA keyboard interrupt has been noticed")
 
except:
	print("\nAn error or exception has occurred!")
 
finally:
	GPIO.cleanup()
