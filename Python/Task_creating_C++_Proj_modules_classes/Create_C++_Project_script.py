import os
from pprint import pprint

your_input = ""
Configuration_container = {}
Class = {
            "ClassName" : "" , 
            "Constructors" : [] , 
            "Data_members" : {"private" : [] , "protected" : [] , "public" : []},
            "Method_members" : {"private" : [] , "protected" : [] , "public" : []}
        }
Module= {'Name' : "" ,"Data" : [] , "Functions" : []}

def configure_data():
    while 1 :
        global Module
        order = input ("Enter Data formated Like this {Name : value} or done to exit :")
        if order == "done" : break
        data_list = order.split(" : ")
        Module["Data"].append(data_list)

def Configure_Func():
    while 1 :
        global Module
        order = input ("Enter Function formated Like this {Name : return : parameters separated by(,)} or done to exit :")
        if order == "done" : break
        data_list = order.split(" : ")
        paramters_list = data_list[2].split(",")
        Func={"Name" : "" , "Return" : "" , "Parameters" : []}
        Func["Name"] = data_list[0]
        Func["Return"] = data_list[1]
        Func["Parameters"].append(paramters_list)
        Module["Functions"].append(Func)
        

def Configure_DataMember(AccessType):
    while 1 : 
        global Class
        order = input(f"Enter {AccessType} Data formated like (Name : Value) or done to exit :")
        if order == "done" : break
        data_list = order.split(" : ")
        Class["Data_members"][AccessType].append(data_list)

def Configure_MethodMember(AccessType):
    while 1 :
        global Class
        order = input (f"Enter {AccessType} method formated Like this (Name : return : parameters separated by(,)) or done to exit :")
        if order == "done" : break
        data_list = order.split(" : ")
        Method = {"Name" : "" , "Return" : "" , "parameters" : []}
        Method["Name"]   = data_list[0]
        Method["Return"] = data_list[1]
        paramters_list = data_list[2].split(",")
        Method["parameters"].append(paramters_list)
        Class["Method_members"][AccessType].append(Method)

while your_input != '2' :
    your_input  = input("Write your command here {configure New project(press 1) / Start Generation(press 2)}: ")
    if your_input == '1' :
        #adding your configurations into storage containers...
        Configuration_container["Directories"] = []
        Configuration_container["files"] = []
        Configuration_container["Classes"] = []
        Configuration_container["Modules"] = []
        Configuration_container["FileType"] = []

        while 1:
            order = input("Do you want to create new {directory(1) , file(2) or break Config(3)} : ")
            
            if order == '1':
                order = input("Directory path :")
                Configuration_container["Directories"].append(order) 
            
            if order == '2':
                order = input("file path with extension :")
                Configuration_container["files"].append(order)
                order = input("the type of this folder is a module(1) or class(2) :")
                
                if order == '1':   #create a module
                    order = input ("Enter Module Name :")
                    Module["Name"] = order
                    configure_data()
                    Configure_Func()
                    Configuration_container["Modules"].append(Module)
                    Configuration_container["FileType"].append("Module")
                    Module= {"Name" :  "" , "Data" : [] , "Functions" : []}
                elif order == '2': #create a class
                    
                    order = input("Enter the class name :")
                    Class["ClassName"] = order

                    order = input("Enter types of constructors {default(1) , parameterized(2)} separated by , : ")
                    constructors_list = order.split(',')
                    Class["Constructors"] = constructors_list
                    
                    Configure_DataMember("private")
                    Configure_DataMember("protected")
                    Configure_DataMember("public")
                    Configure_MethodMember("private")
                    Configure_MethodMember("protected")
                    Configure_MethodMember("public")
                    Configuration_container["Classes"].append(Class)
                    Configuration_container["FileType"].append("Class")
                    Class = {
                                "ClassName" : "" , 
                                "Constructors" : [] , 
                                "Data_members" : {"private" : [] , "protected" : [] , "public" : []},
                                "Method_members" : { "private" : [] , "protected" : [] , "public" : []}
                            } 

            elif order == '3':
                break
    
    # Configuration_container = {'Classes': [
    #                                         {'ClassName': 'Welcome',
    #                                          'Constructors': ['1 ', ' 2'],
    #                                          'Data_members': {'private': [['int x', '10']],
    #                                                           'protected': [['int y', '20']],
    #                                                           'public': [['float r', '5.7']]},
    #                                          'Method_members': {
    #                                                             'private': [
    #                                                                          {
    #                                                                          'Name': 'tt',
    #                                                                          'Return': 'void',
    #                                                                          'parameters': [['int h']]
    #                                                                          }
    #                                                                         ],
    #                                                             'protected': [
    #                                                                           {
    #                                                                           'Name': 't2',
    #                                                                           'Return': 'int',
    #                                                                           'parameters': [['int h']]
    #                                                                           }
    #                                                                          ],
    #                                                             'public': [
    #                                                                          {
    #                                                                          'Name': 't3',
    #                                                                          'Return': 'void',
    #                                                                          'parameters': [['int h ', ' int y']]
    #                                                                          }
    #                                                                       ]
    #                                                             }
    #                                         }
    #                                        ],
    #                             'Directories': [
    #                                             '~/Documents/NewProj',
    #                                             '~/Documents/NewProj/Cfile',
    #                                             '~/Documents/NewProj/CppFile'
    #                                             ],
    #                             'Modules': [
    #                                         {
    #                                          'Name': "hello.h",
    #                                          'Data': [['int x', '10'], ['int y', '20'], ['float z', '20.5']],
    #                                          'Functions': [
    #                                                        {'Name': 'sum','Parameters': [['int x ', ' int y']],'Return': 'int'},
    #                                                        {'Name': 'diff','Parameters': [['int x ', ' int y']],'Return': 'int'}
    #                                                       ]
    #                                         }
    #                                        ],
    #                             'files': [
    #                                       '~/Documents/NewProj/Cfile/hello.h',
    #                                       '~/Documents/NewProj/CppFile/CP.h'
    #                                      ],
    #                             'FileType' : ["Module" , "Class"]
    #                           }
    pprint(Configuration_container)
        
    if your_input == '2':
        #generate new project...
        ###############################################################
        #creating directories..
        for dir in Configuration_container["Directories"] :
            try:
                expanded_directory = os.path.expanduser(dir)
                os.mkdir(expanded_directory)
                print(f"Directory '{dir}' created successfully.")
            except FileExistsError:
                print(f"Directory '{dir}' already exists.")
            except FileNotFoundError:
                print(f"The specified path does not exist: {dir}")
        #creating Files
        Module_index = 0 
        Class_index = 0
        for i in range(0 , len(Configuration_container["files"])) : 
            file_path = os.path.expanduser(Configuration_container["files"][i])
            with open(file_path,'+w') as F:
                #create .h , .c file 
                if(Configuration_container["FileType"][i] == "Module"):
                   
                   mod = Configuration_container["Modules"][Module_index]
                   File_dot_c = file_path.replace(".h",".c")
                   
                   #Fill .h file..
                   F.writelines("#include <stdio>\n")
                   F.writelines("\n\n")
                   for mod_Func in mod["Functions"]:
                      param_str = " , ".join(mod_Func["Parameters"][0])
                      r = mod_Func["Return"]
                      n = mod_Func["Name"]
                      F.writelines(f"{r} {n} ({param_str}) ;\n\n")

                   #Fill .c file..
                   with open(File_dot_c,'+w') as FC:
                        module_name = Configuration_container['Modules'][Module_index]["Name"]
                        FC.writelines(f"#include <{module_name}>\n")
                        FC.writelines("\n\n")
                        for mod_Data in mod["Data"]:
                            FC.writelines(f"{mod_Data[0]} = {mod_Data[1]}\n")
                        for mod_Func in mod["Functions"]:
                            param_str = ",".join(mod_Func["Parameters"][0])
                            r = mod_Func["Return"]
                            n = mod_Func["Name"]
                            FC.write(f"{r} {n} ({param_str})")
                            FC.write("{\n} \n\n")

                   Module_index+=1
                #create .h , .cpp file 
                elif(Configuration_container["FileType"][i] == "Class"):
                   cl = Configuration_container["Classes"][Class_index]
                   File_dot_cpp = file_path.replace(".h",".cpp")
                   #Fill .h file..
                   F.writelines("#include <std>\n")
                   F.writelines("\n\n")
                   class_name = cl["ClassName"]
                   F.write(f"class {class_name}")
                   F.write("{\n")

                   #constructors ..
                   Class_Data=[]
                   Constructor_Param = []
                   for type_access in cl["Data_members"]: 
                       for x in cl["Data_members"][type_access] :
                           tempList = x[0].split(" ")
                           Class_Data.append(tempList[-1])
                           Constructor_Param.append(x[0])
                   for constructor in cl["Constructors"] :
                       if constructor.strip() == '1' : #default..
                           F.write(f"{class_name} ()")
                           F.write("{}\n")
                       else: #parameterized..
                           ConstructorParam_tuple = " , ".join(Constructor_Param)
                           F.write(f"{class_name} ({ConstructorParam_tuple}) : ")
                           for val in Class_Data:
                                F.write(f"{val}")
                                F.write("{")
                                F.write(f"{val}")
                                F.write("}")
                                if(val != Class_Data[-1]):
                                    F.write("} ,")
                           F.write("{} \n")
                   #Build the rest of the class ...        
                   F.write("private : \n")
                   for cl_Private_Data in cl["Data_members"]["private"]:
                      temp_data = cl_Private_Data[0] + " = " + cl_Private_Data[1] + ";"
                      F.write(f"{temp_data}\n")
                   for cl_Private_Func in cl["Method_members"]["private"]:
                      temp_data = cl_Private_Func["Return"] +" "+ cl_Private_Func["Name"] 
                      param_str = ",".join(cl_Private_Func["parameters"][0])
                      F.write(f"{temp_data}({ param_str}) ;\n")
                   F.write("protected : \n")
                   for cl_Protected_Data in cl["Data_members"]["protected"]:
                      temp_data = cl_Protected_Data[0] + " = " + cl_Protected_Data[1] + ";"
                      F.write(f"{temp_data}\n")
                   for cl_Protected_Func in cl["Method_members"]["protected"]:
                      temp_data = cl_Protected_Func["Return"] + " " + cl_Protected_Func["Name"] 
                      param_str = ",".join(cl_Protected_Func["parameters"][0])
                      F.write(f"{temp_data}({param_str}) ;\n")
                   F.write("public : \n")
                   for cl_public_Data in cl["Data_members"]["public"]:
                      temp_data = cl_public_Data[0] + " = " + cl_public_Data[1] + ";"
                      F.write(f"{temp_data}\n")
                   for cl_public_Func in cl["Method_members"]["public"]:
                      temp_data = cl_public_Func["Return"] + " " +cl_public_Func["Name"] 
                      param_str = ",".join(cl_public_Func["parameters"][0])
                      F.write(f"{temp_data}({param_str}) ;\n")
                   F.write("\n };")

                   #Fill .cpp file..
                   with open(File_dot_cpp,'+w') as FC:
                        Class_name = Configuration_container['Classes'][Class_index]["ClassName"]
                        FC.writelines(f"#include <{Class_name}>\n")
                        FC.writelines("\n\n")
                        for class_Func_list in Configuration_container['Classes'][Class_index]["Method_members"]:
                            for class_Func in Configuration_container['Classes'][Class_index]["Method_members"][class_Func_list]:
                                param_str = ",".join(class_Func["parameters"][0])
                                r = class_Func["Return"]
                                n = class_Func["Name"]
                            FC.write(f"{r} {n} ({param_str})")
                            FC.write("{\n} \n")
                   Class_index+=1

