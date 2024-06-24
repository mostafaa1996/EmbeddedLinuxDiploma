#!/usr/bin/python3
#Write a Python program to count the number 4 in a given list.
ls  = input("Write a random collection of numbers : ").split(" ")
ls2 = [int(i) for i in ls ] 
print(ls2,"\n",ls2.count(4))
