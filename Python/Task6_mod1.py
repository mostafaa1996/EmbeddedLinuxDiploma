#!/usr/bin/python3
#Make your module that contain favourite websites and have function called Firefox take url and open website
#then make main file and print menu of sites for user and let him choice

import webbrowser

dic_fav_webs = {
"Youtube" : "https://www.youtube.com/" ,
"Gmail"   :"https://mail.google.com/mail/u/0/#inbox" ,
"LinkedIn":"https://www.linkedin.com/feed/" ,
"Teams"   :"https://teams.microsoft.com/v2/?culture=ar-sa" ,
"Facebook":"https://www.facebook.com/"
}

def firefox(webPage):
    webbrowser.open(webPage)
    