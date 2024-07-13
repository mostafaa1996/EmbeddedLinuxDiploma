import os
from pprint import pprint

Configuration_container = {}
Class = {
            "ClassName" : "" , 
            "Constructors" : [] , 
            "Data_members" : {"private" : [] , "protected" : [] , "public" : []},
            "Method_members" : {"private" : [] , "protected" : [] , "public" : []}
        }
Module= {'Name' : "" ,"Data" : [] , "Functions" : []}
Configuration_container["Directories"] = []
Configuration_container["files"] = []
Configuration_container["Classes"] = []
Configuration_container["Modules"] = []
Configuration_container["FileType"] = []
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
    
# {'Classes': [
    
#     {'ClassName': 'Hello',
#      'Constructors': ['1', '2'],
#      'Data_members': {'private': ['char x = 0'],'protected': ['unsigned int y = 0'],'public': ['float g = 0']},
#      'Method_members': {'private': ['int f1(int x)'],'protected': ['char f2(int x , int i)'],'public': ['BaseClass* f3()']}
#     }       
#             ],
#  'Directories': ['C:/Users/E0162630/Desktop',
#                  'C:/Users/E0162630/Desktop/NewCp\n'],
#  'FileType': ['Class'],
#  'Modules': [{'Data': [], 'Functions': [], 'Name': ''}],
#  'files': ['C:/Users/E0162630/Desktop/NewCp/Hello.h']
#  }
        
def Generation():
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
                       F.writelines(f"{mod_Func} ;\n\n")

                   #Fill .c file..
                   with open(File_dot_c,'+w') as FC:
                        module_name = Configuration_container['Modules'][Module_index]["Name"]
                        FC.writelines(f"#include <{module_name}.h>\n")
                        FC.writelines("\n\n")
                        for mod_Data in mod["Data"]:
                            FC.writelines(f"{mod_Data}\n")
                        for mod_Func in mod["Functions"]:
                            F.writelines(f"{mod_Func}")
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
                   for constructor in cl["Constructors"] :
                       if constructor.strip() == '1' : #default..
                           F.write(f"{class_name} ()")
                           F.write("{\n")
                           for dataInType in cl["Data_members"].values() :
                               for data in dataInType:
                                   F.write(f"{data}\n")
                           F.write("\n}\n")
                       else: #parameterized..
                           ParameterizeList = []
                           ElementsList = []
                           for dataInType in cl["Data_members"].values() :
                               for data in dataInType:
                                   ParameterizeList.append(data[0 : data.find("=")])
                                   temp_str = ((data[0 : data.find("=")]).split(" "))[-1]
                                   ElementsList.append(temp_str)
                           ParameterizeList_str = ",".join(ParameterizeList)
                           F.write(f"{class_name} ({ParameterizeList_str}) : ")
                           for val in ElementsList:
                                F.write(f"{val}")
                                F.write("{")
                                F.write(f"{val}")
                                F.write("}")
                                if(val != ElementsList[-1]):
                                    F.write(",")
                           F.write("{} \n")
                   #Build the rest of the class ...        
                   F.write("private : \n")
                   for cl_Private_Data in cl["Data_members"]["private"]:
                      temp_data = cl_Private_Data[0 : cl_Private_Data.find("=")]
                      F.write(f"{temp_data} ; \n")
                   for cl_Private_Func in cl["Method_members"]["private"]:
                      F.write(f"{cl_Private_Func} ;\n")
                   F.write("protected : \n")
                   for cl_Protected_Data in cl["Data_members"]["protected"]:
                      temp_data = cl_Protected_Data[0 : cl_Protected_Data.find("=")]
                      F.write(f"{temp_data} ; \n")
                   for cl_Protected_Func in cl["Method_members"]["protected"]:
                      F.write(f"{cl_Protected_Func} ;\n")
                   F.write("public : \n")
                   for cl_public_Data in cl["Data_members"]["public"]:
                      temp_data = cl_public_Data[0 : cl_public_Data.find("=")]
                      F.write(f"{temp_data} ; \n")
                   for cl_public_Func in cl["Method_members"]["public"]:
                      F.write(f"{cl_public_Func} ;\n")
                   F.write("\n };")

                   #Fill .cpp file..
                   with open(File_dot_cpp,'+w') as FC:
                        Class_name = Configuration_container['Classes'][Class_index]["ClassName"]
                        FC.writelines(f"#include <{Class_name}>\n")
                        FC.writelines("\n\n")
                        for FuncScope in Configuration_container['Classes'][Class_index]["Method_members"].keys():
                            for class_Func in Configuration_container['Classes'][Class_index]["Method_members"][FuncScope]:
                                #example I have unsigned int x(int y ,int z) -------> I need to convert them to unsigned int Configuration::x(int y ,int z)
                                InsertionString = f"{Class_name}::" #Configuration::
                                PosOffirstPartInParam = class_Func.find("(")
                                temp_str = class_Func[0:PosOffirstPartInParam] # unsigned int x
                                List_temp_str = temp_str.split(" ") # ['unsigned' , 'int' ,  'x']
                                funcName = List_temp_str[-1] # x
                                PosOffuncName = class_Func.find("funcName")
                                class_Func_Modified = class_Func[:PosOffuncName] + InsertionString + class_Func[PosOffuncName:]
                                # ParamString = class_Func[class_Func.find("(") : ]
                                FC.write(f"{class_Func_Modified}")
                                FC.write("{\n} \n")
                            
                   Class_index+=1

