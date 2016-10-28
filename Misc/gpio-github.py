#!/usr/bin/python


# Imports
import requests
from sys import version_info
import RPi.GPIO as GPIO
import time


# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

py3 = version_info[0] > 2
if py3:
	user = input('Enter a GitHub username(i.e. Belax8): ')
else:
	user = raw_input('Enter a GitHub username(i.e. Belax8): ')


# User Request
user_url = 'https://api.github.com/users/' + user
content = requests.get(user_url).json()

# Blink once for each follower
for x in range(0, content['followers']):
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)
	time.sleep(1)

print(str(content['followers']) + ' Followers')

GPIO.cleanup()
