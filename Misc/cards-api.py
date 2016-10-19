#!/usr/bin/python

"""
Check out this cool API at https://deckofcardsapi.com
"""


# Imports
import requests


# Initial request for new deck
new_deck_url = 'https://deckofcardsapi.com/api/deck/new/shuffle'
content = requests.get(new_deck_url).json()


# Setup variables
deck_id = content['deck_id']
main_url = 'https://deckofcardsapi.com/api/deck/' + deck_id + '/draw/?count=5'


# Get User's cards
user_cards = requests.get(main_url).json()


# Get Computer's cards
computer_cards = requests.get(main_url).json()


# Print Info
print('Your cards:')

for m in user_cards['cards']:
	print(m['value'] + ' of ' + m['suit'])

print('')
print("Computer's Cards:")

for i in computer_cards['cards']:
	print(i['value'] + ' of ' + i['suit'])

