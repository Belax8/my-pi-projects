#!/usr/bin/python


# Imports
import os


# Run pi-temp.py multiple times in the background
os.system('python pi-temp.py &')
os.system('python pi-temp.py &')
os.system('python pi-temp.py &')
os.system('python pi-temp.py &')


# write `ps -ef` to see all the scripts running

# write `kill -9 <id>` to stop a background script
