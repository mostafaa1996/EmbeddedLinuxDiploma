#!/usr/bin/python3
'''
shebang... it`s a way to identify that this file is a python file while executing it using terminal 
through this command (./filename.py)
'''
import dis
# from gtts import gTTS
# import os
# os.environ['VLC_PLUGIN_PATH'] = '/usr/lib/vlc/plugins'
# import vlc
# myobj = gTTS(text = 'صباح الخير يا مصطفى ', lang = 'ar' , slow = False)
# myobj.save("Welcome.mp4")
# p = vlc.MediaPlayer("/home/mostafa/Documents/Newfolder/Welcome.mp4")
# p.play()
# while True :
#     pass

print("Hello")
def f(x):
    return x+1 
dis.dis(f)
print(f.__code__.co_code)
print(hex(dis.opmap['LOAD_FAST']))
string = "Mostafa hamdy is 27 years old."
print(list(string))

def my_fun(*arg):
    x = arg[0]
    print(x)
my_list = ["mostafa" , "hamdy" , 27]
my_fun(*my_list)