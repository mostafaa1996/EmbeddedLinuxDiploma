#!/usr/bin/python3
#Write a python program to access environment variables.
import os

os.environ['MY_New_Val'] = "MostafaHamdy"
print(os.environ.get('MY_New_Val'))
del os.environ['MY_New_Val']
print(os.environ.get('MY_New_Val'))