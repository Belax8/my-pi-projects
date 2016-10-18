#!/usr/bin/python


# Imports
import requests


# Get request
url = 'https://api.icndb.com/jokes/random'
r = requests.get(url).json()


# Print the joke
print('')
print(r['value']['joke'])
print('')
