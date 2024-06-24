#!/usr/bin/python3
"""
Using PyAutoGUI
- To open vscode
- install clangd from extension
- install c++ testmate from extension
- install c++ helper from extension
- install cmake from extension
- install cmake tools from extension
"""
import pyautogui as p 
from time import sleep
sleep(1)
Not_Found_Flag = False
Extension_list = ["C++ Clangd" , "C++ Helper" , "C++ TestMate" , "CMake" , "CMake Tools"]
def Access_Icons(Icon):
    global Not_Found_Flag
    count = 0
    while True :
        try :
            loc = p.locateCenterOnScreen(Icon,confidence=0.8)
            sleep(1)
            break
        except:
            count+=1
            sleep(1)
            if(count >5): 
                Not_Found_Flag = True
                break
    if(Not_Found_Flag == False):
        p.moveTo(loc)
        p.click()

def Access_Search(SearchPhoto , SearchAfterPhoto):
    global Not_Found_Flag
    Access_Icons(SearchPhoto)
    if(Not_Found_Flag):
        Not_Found_Flag = False
        Access_Icons(SearchAfterPhoto)
    if(Not_Found_Flag == False):
        p.hotkey('ctrl','a')
        sleep(1)
        p.hotkey('backspace')
        sleep(1)
###########VS access#################
Access_Icons("VS.png")
###########Search Icon access#################
Access_Search("Search.png","SearchAfter.png")
###########Extension Icon access#################
if(Not_Found_Flag):
    Not_Found_Flag = False
    Access_Icons("ExtensionIcon.png")
    Access_Search("Search.png" , "SearchAfter.png")
    
for item in Extension_list:
    if(Not_Found_Flag==False):
        p.write(item)
        p.press('enter')
        Access_Icons(item.replace(" ","")+".png")
        sleep(2)
        try : 
            Disable_loc = p.locateCenterOnScreen("Disable.png",confidence=0.8)
            sleep(2)
            print(f"DisableIcon at : {Disable_loc}")
            Access_Search("SearchAfter.png","Search.png")
        except :
            try:
                Install_loc = p.locateCenterOnScreen("Install.png",confidence=0.8)
                sleep(2)
                print(f"Install Icon at : {Install_loc}")
                p.moveTo(Install_loc) #x=2050,y=225
                p.click()
                sleep(3)
                Access_Search("Search.png" , "SearchAfter.png")
            except:
                pass
            
        
            
#p.mouseInfo()
            