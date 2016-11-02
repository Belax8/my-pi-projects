#!/usr/bin/python

# Imports
import requests
import json


# Make Request
url = 'http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=jsonp&lang=en&jsonp=?'
data = requests.get(url)


# Format data
data = data.content[2:]
data = data[:-1]
data = json.loads(data)


# Display data
print('')
print(data['quoteText'])
print('By, ' + data['quoteAuthor'])
print('')
