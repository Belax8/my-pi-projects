#!/usr/bin/python


# Imports
import requests
from sys import version_info
import json


# Setup
py3 = version_info[0] > 2
if py3:
	search_text = input('What would you like to search? ')
else:
	search_text = raw_input('What would you like to search? ')


# Request
url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit=10&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=1&exlimit=max&gsrsearch=' + search_text + '&callback=?'
req = requests.get(url)


# Edit data to be able to convert it to JSON
data = req.content[5:]
data = data[:-1]
data = json.loads(data)


# Print Data
print('')
if 'query' in data:
	content = data['query']['pages']
	for x in content:
		print('Title: ' + content[x]['title'])
		print('Extract: ' + content[x]['extract'])
		#print('URL: ' + content[x][''])
		print('')
else:
	print('There are no results for your search.')
	print('')
