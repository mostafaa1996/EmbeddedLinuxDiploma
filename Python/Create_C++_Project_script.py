import os
from pprint import pprint
your_input = ""
Configuration_container = {}
while your_input != '2' :
    your_input  = input("Write your command here {configure New project(press 1) / Start Generation(press 2)}: ")
    if your_input == '1' :
        #adding your configurations into storage containers...
        Configuration_container["Directories"] = []
        Configuration_container["files"] = []
        Configuration_container["FileType"] = []
        Configuration_container["ClassName"] = []
        Configuration_container["ClassContent"] = {
                                                   "private"   : {"Data" : {} , "methods":{"Name":[],"Return":[],"Parameters": []}},
                                                   "protected" : {"Data" : {} , "methods":{"Name":[],"Return":[],"Parameters": []}}, 
                                                   "public"    : {"Data" : {} , "methods":{"Name":[],"Return":[],"Parameters": []}},
                                                   "ListOfConstructors" : []
                                                  }
        Configuration_container["ModuleContent"] = {
                                                   "Data" : {} , 
                                                   "Func" : {"Name":[],"Return":[],"Parameters": [[]]}
                                                   }
        while 1:
            order = input("Do you want to create new {directory(1) , file(2) or break Config(3)} : ")
            
            if order == '1':
                order = input("Directory path :")
                Configuration_container["Directories"].append(order) 
            
            if order == '2':
                order = input("file path with extension :")
                Configuration_container["files"].append(order)
                order = input("the type of this folder is a module(1) or class(2) :")
                if order == '1':
                    Configuration_container["FileType"].append("Module")
                    while 1 :
                        order = input ("Enter Data formated Like this {Name : value} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ModuleContent"]["Data"][data_list[0]] = data_list[1]
                    while 1 :
                        order = input ("Enter Function formated Like this {Name : return : parameters separated by(,)} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ModuleContent"]["Func"]["Name"] = data_list[0]
                        Configuration_container["ModuleContent"]["Func"]["Return"] = data_list[1]
                        paramters_list = data_list[2].split(",")
                        Configuration_container["ModuleContent"]["Func"]["parameters"].append(paramters_list)
                elif order == '2':
                    Configuration_container["FileType"].append("Class")
                    order = input("Enter the class name :")
                    Configuration_container["ClassName"] = order
                    while 1 : 
                        order = input("Enter private Data formated like {Name : Value} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["private"][data_list[0]] = data_list[1]
                    while 1 : 
                        order = input("Enter protected Data formated like {Name : Value} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["protected"][data_list[0]] = data_list[1]
                    while 1 : 
                        order = input("Enter public Data formated like {Name : Value} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["public"][data_list[0]] = data_list[1]
                    while 1 :
                        order = input ("Enter private method formated Like this \
                                       {Name : return : parameters separated by(,)} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["private"]["methods"]["Name"]   = data_list[0]
                        Configuration_container["ClassContent"]["private"]["methods"]["Return"] = data_list[1]
                        paramters_list = data_list[2].split(",")
                        Configuration_container["ClassContent"]["private"]["methods"]["parameters"].append(paramters_list)
                    while 1 :
                        order = input ("Enter protected method formated Like this \
                                       {Name : return : parameters separated by(,)} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["protected"]["methods"]["Name"]   = data_list[0]
                        Configuration_container["ClassContent"]["protected"]["methods"]["Return"] = data_list[1]
                        paramters_list = data_list[2].split(",")
                        Configuration_container["ClassContent"]["protected"]["methods"]["parameters"].append(paramters_list)
                    while 1 :
                        order = input ("Enter public method formated Like this \
                                       {Name : return : parameters separated by(,)} or done to exit :")
                        if order == "done" : break
                        data_list = order.split(" : ")
                        Configuration_container["ClassContent"]["public"]["methods"]["Name"]   = data_list[0]
                        Configuration_container["ClassContent"]["public"]["methods"]["Return"] = data_list[1]
                        paramters_list = data_list[2].split(",")
                        Configuration_container["ClassContent"]["public"]["methods"]["parameters"].append(paramters_list)

            elif order == '3':
                break
    
    pprint(Configuration_container)

    if your_input == '2':
        #generate new project...
        pass

