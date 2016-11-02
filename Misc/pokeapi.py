#!/usr/bin/python


# Imports
import requests
from sys import version_info


# Setup
py3 = version_info[0] > 2

if py3:
	pokemon = input('Which pokemon would you like to look up? ')
else:
	pokemon = raw_input('Which pokemon would you like to loop up? ')


# Make Request
url = 'http://pokeapi.co/api/v2/pokemon/' + pokemon
req = requests.get(url)
data = req.json()


# Display data
print('')
if req.status_code != 200:
	print('Sorry that pokemon doesn\'t exist')
else:
	print('Name: ' + data['name'].title())
	print('Height: ' + str(data['height']))
	print('Weight: ' + str(data['weight']))
	print('Base Experience: ' + str(data['base_experience']))

	print('')
	print('Abilities:')
	for x in data['abilities']:
		print(' * ' + x['ability']['name'])

	print('')
	print('Held Items:')
	for n in data['held_items']:
		print(' * ' + n['item']['name'])

print('')
