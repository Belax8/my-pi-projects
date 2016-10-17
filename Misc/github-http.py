#!/usr/bin/python

"""
This Script will print info about the given GitHub user below
"""
user = 'Belax8'


# Imports
import urllib2, json


# User Request
userUrl = 'https://api.github.com/users/' + user
userRes = urllib2.urlopen(userUrl).read()
content = json.loads(userRes)


# Print user info
print('Name: ' + content['login'])

if content['company'] != None:
	print('Company: ' + content['company'])

if content['bio'] != None:
	print('Bio: ' + content['bio'])

print('Followers: ' + str(content['followers']))


# Get Organization info
orgUrl = content['organizations_url']
orgRes = urllib2.urlopen(orgUrl).read()
orgContent = json.loads(orgRes)


# Print User Organization info
for org in orgContent:
	print('Organization: ' + org['login'])
