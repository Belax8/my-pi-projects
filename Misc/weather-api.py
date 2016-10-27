#!/usr/bin/python


# Imports
import requests


# Setup
zip_code = raw_input("Which zip code would you like to check the weather of? ")
api_key = 'fc8ae934cc756cb097a187d5a0b3e428'
url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zip_code + ',us&APPID=' + api_key + '&units=imperial'


# Request
weather = requests.get(url).json()


# Print Info
print('Location: ' + weather['name'])
print('Weather: ' + weather['weather'][0]['description'])
print('Wind: ' + str(weather['wind']['speed']) + 'MPH')
print('Temperature: ' + str(weather['main']['temp']) + 'F')