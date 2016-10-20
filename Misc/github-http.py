#!/usr/bin/python

"""
This Script will print info about the given GitHub user below
"""
user = raw_input('Enter a GitHub username(i.e. Belax8): ')

# Imports
import requests


# User Request
user_url = 'https://api.github.com/users/' + user
user_res = requests.get(user_url)
content = user_res.json()


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
		print('Organization: ' + org['login'])
