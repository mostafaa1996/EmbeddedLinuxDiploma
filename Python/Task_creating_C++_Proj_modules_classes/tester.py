import pyautogui as p 
from time import sleep
sleep(3)
input_list = ["1" , "1" ,"~/Documents/NewProj" , "1" , 
              "~/Documents/NewProj/Cfile" , "1" ,
              "~/Documents/NewProj/CppFile" , "2",
              "~/Documents/NewProj/Cfile/hello.h", "1" , "hello.h",
              "int x : 10" , "int y : 20" , "float z : 20.5" , "done" ,
              "sum : int : int x , int y" , "diff : int : int x , int y" , "done" , "2" , 
              "~/Documents/NewProj/CppFile/CP.h" , "2" ,
              "Welcome" , "1 , 2", "int x : 10" , "done" , "int y : 20" , "done" , "float r : 5.7" , "done",
              "tt : void : int h" , "done" , "t2 : int : int h" , "done" , "t3 : void : int h , int y" , "done" , "3"]
print(len(input_list))
for i in range(0 , len(input_list) , 1):
    while 1 : 
        try :
            cursor_loc = p.locateCenterOnScreen("Cursor.png" , confidence= 0.8)
            break
        except:
            sleep(0.5)
    
    p.moveTo(cursor_loc)
    sleep(0.5)
    p.click()
    p.write(input_list[i])
    p.press('enter')
    sleep(0.5)