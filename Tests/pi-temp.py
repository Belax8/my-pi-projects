#!/usr/bin/python

# This isn't really an infinite loop
# It will keep looping til it finds the first 100,000 prime numbers

# Imports
import os

# Change count if you want to run this more or less
count = 5

os.system('python basic-temp.py')

for x in range(0,count):
	is_active = True
	array = []
	n = 2

	while is_active:
        	# Find primes and append them to array
        	i = 1
        	while i <= n:
                	j = 2
                	while j <= i:
                        	if j == i:
                                	array.append(i)
                        	if i % j == 0:
                                	break
                        	j += 1
                	i += 1
        	# This will make it wait for a while
        	if len(array) > 99999:
                	is_active = False

        	n += 1
	
	os.system('python basic-temp.py')
