#!/usr/bin/python3
#Write a Python program to test whether a passed letter is a vowel or not.
set_vowel_char = {'A','E','O','U','I'}
input_letter  = input("Enter a single letter only : ")
if (input_letter.upper() in set_vowel_char):
    print(True)
else:
    print(False)
    ###############################################
    
