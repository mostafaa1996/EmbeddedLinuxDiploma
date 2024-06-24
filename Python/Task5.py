#!/usr/bin/python3
#Print the calendar of a given month and year

import calendar
year = int(input("Enter the year number : "))
month = int(input("Enter the month number : "))
print(calendar.month(year , month ))


