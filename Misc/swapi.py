#!/usr/bin/python


# Imports
import requests
from sys import version_info


# Setup
py3 = version_info[0] > 2
if py3:
	person = input('Which Star Wars character would you like to find? ')
else:
	person = raw_input('Which Star Wars character would you like to find? ')


# Make request
url = 'http://swapi.co/api/people/?search=' + person
req = requests.get(url)
data = req.json()


# Helper functions
def display_one_character():
	# Print info
        print('Name: ' + data['results'][0]['name'])
        print('Height: ' + data['results'][0]['height'])
        print('Mass: ' + data['results'][0]['mass'])
	print('Birth Year: ' + data['results'][0]['birth_year'])
	print('Gender: ' + data['results'][0]['gender'])
	# Get species info
	species_url = data['results'][0]['species'][0]
	species_data = requests.get(species_url).json()
	print('Species: ' + species_data['name'])
	print('Classification: ' + species_data['classification'])
	print('Language: ' + species_data['language'])

def display_list():
        print('Here are the characters we found:')
        for x in data['results']:
                print(x['name'])

def no_character_available():
	print('We couldn\'t find anyone with that name. Sorry.')


# Display data
if req.status_code != 200:
	print('')
	no_character_available()
	print('')
else:
	print('')
	if data['count'] == 0:
		no_character_available()
	elif data['count'] == 1:
		display_one_character()
	else:
		display_list()
	print('')

