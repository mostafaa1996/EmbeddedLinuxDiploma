#!/usr/bin/python3
#Make your module that contain favourite websites and have function called Firefox take url and open website
#then make main file and print menu of sites for user and let him choice

import Task6_mod1 as firefoxMachine
#url = firefoxMachine.dic_fav_webs["Youtube"]
url_key = input(f"Enter your favourite website to open from this list {firefoxMachine.dic_fav_webs.keys()} : ").lower()
url = ""
for i in firefoxMachine.dic_fav_webs.keys():
    if(url_key == i.lower()):
        url = firefoxMachine.dic_fav_webs[i]
if(bool(url) == False):
    print("you should select the favourite website from our list or you need to add it. ")
else:
    firefoxMachine.firefox(url)

