#!/usr/bin/python


# Import
import RPi.GPIO as GPIO
import time


# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)


# Helper functions
def flash_lights():
	# Turn light on 
	GPIO.output(17, True)

	# Wait
	time.sleep(1)

	# Turn light off
	GPIO.output(17, False)

	time.sleep(1)


# Run Loop
try:
	while True:
		flash_lights()

# Cleanup
except KeyboardInterrupt:
	print("\nA keyboard interrupt has been noticed")
 
except:
	print("\nAn error or exception has occurred!")
 
finally:
	GPIO.cleanup()
