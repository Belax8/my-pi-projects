#!/usr/bin/python


# Imports
import requests
from sys import version_info


# Setup
py3 = version_info[0] > 2
if py3:
	zip_code = input('Which zip code would you like to check the weather of? ')
else:
	zip_code = raw_input("Which zip code would you like to check the weather of? ")
api_key = 'fc8ae934cc756cb097a187d5a0b3e428'
url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip_code + ',us&APPID=' + api_key + '&units=imperial'


# Request
data = requests.get(url)
weather = data.json()


# Print Info
if data.status_code != 200:
	print('Error. We could not find this location.')
else:
	print('Location: ' + weather['name'])
	print('Weather: ' + weather['weather'][0]['description'])
	print('Wind: ' + str(weather['wind']['speed']) + 'MPH')
	print('Temperature: ' + str(weather['main']['temp']) + 'F')
