#!/usr/bin/python

"""
This Script will print info about the given GitHub user below
"""

# Imports
import requests
from sys import version_info


# Setup
py3 = version_info[0] > 2
if py3:
	user = input('Enter a GitHub username(i.e. Belax8): ')
else:
	user = raw_input('Enter a GitHub username(i.e. Belax8): ')


# User Request
user_url = 'https://api.github.com/users/' + user
user_res = requests.get(user_url)
content = user_res.json()


# Display Data
print('')
if user_res.status_code != 200:
	print("This GitHub user doesn't exist")
else:
	# Print user info
	print('Name: ' + content['login'])

	if content['company'] != None:
		print('Company: ' + content['company'])

	if content['bio'] != None:
		print('Bio: ' + content['bio'])

	print('Followers: ' + str(content['followers']))


	# Get Organization info
	org_url = content['organizations_url']
	org_res = requests.get(org_url)
	org_content = org_res.json()


	# Print User Organization info
	for org in org_content:
		print('')
		org_info_url = org['url']
		org_info = requests.get(org_info_url).json()
		print('Organization: ' + org_info['name'])
		if len(org_info['description']) > 1:
			print('Description: ' + org_info['description'])
		print('Website: ' + org_info['blog'])
print('')
