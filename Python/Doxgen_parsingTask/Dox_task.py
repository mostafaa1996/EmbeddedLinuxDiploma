from bs4 import BeautifulSoup as Bsoup
from pprint import pprint
import pandas
special_tags = ["<b>" , "<br/>" , "<li>"]
ModuleFunc_list = [] #list of Funcs
RowData = {          #dataBase for excelSheet..
   "ModuleName" : "" ,
   "fileType" : "" ,
   "Functions" : []
}
Func = { #single Func doxygen information..
       "FunctionName" : "" ,
       "return"       : "" ,
       "Params"       : [] ,
       "ReturnDes"    : "" ,
       "ParametersDes[in]"  : [] ,
       "ParametersDes[out]" : [] ,
       "Precondition" : "" ,
       "Postcondition": "" ,
       "Description"  : "" ,
       "HistoryOfChanges" : {
          "Date" : "" ,
          "Software Version" : "" ,
          "Initials" : "" ,
          "Description" : ""
       }
}

def Pre_PostConditionsFound(Sectionstring , KeyString):
   temp = i.find("div" , {"class" : "memdoc"}).find("dl" , {"class" : Sectionstring}).find("dd")
   if(len(temp.contents)==0):
      Func[KeyString] = " - " #No precondition exists
   for dd_content in temp :
    if(dd_content.find("<ol")!=-1):
        Pre_list = temp.find_all("li")
        index_Pre_list = 1
        for PreItem in Pre_list:
            Func[KeyString] += f"{index_Pre_list}. " + PreItem.text + "\n"   
            index_Pre_list+=1
        break 
    elif(dd_content != "\n"):
        Func[KeyString] = temp.text #there only one precondition step
        break
            
with open("./Python/Doxgen_parsingTask/html/_file_8c.html" , 'r') as file :
    Content = file.read()
    soup = Bsoup(Content , "lxml")
    Module = soup.find("head").find("title").text
    ModuleName = Module[0:Module.index(":")].strip()
    ModuleType = Module[Module.index(":")+1 : Module.index(".")+2].strip()
    Func_Info  = soup.find_all("div" , {"class" : "memitem"})
    for i in Func_Info :
      ############################Function name , return , parameters #########################################
      memname = i.find("table" , {"class" : "memname" }).find("td" , {"class" : "memname"}).text.strip()
      memParamType_list = i.find("table" , {"class" : "memname" }).find_all("td" , {"class" : "paramtype"})
      memParamName_list = i.find("table" , {"class" : "memname" }).find_all("td" , {"class" : "paramname"})
      if(memParamType_list and memParamName_list):
         Func["FunctionName"] = memname[memname.index(" "):]
         Func["return"]       = memname[0:memname.index(" ")]
         for param_index in range(0,len(memParamType_list)) : 
           memParamType = memParamType_list[param_index].text.strip()
           memParamName = memParamName_list[param_index].find("span" , {"class" : "paramname"}).text.strip()
           Func["Params"].append(memParamType + " " +memParamName)
        #  r = Func["return"]
        #  n = Func["FunctionName"]
        #  l = Func["Params"]
        #  print (f"Return : {r}############ FunctionName : {n} ##########params : {l}")
      ############################################################################################################
      ############################Description#########################################
         Des_list = []
         No_special_tag_found = True
         temp = i.find("div" , {"class" : "memdoc"}).find_all("p") #I have a problem when I search for <p> because it will not return description only it will return 
         #unwanted items has special tags so I need to filter out these paragraghs that include special tags. 
         for ii in temp:
            No_special_tag_found = True
            for special_tag in special_tags :
               for content in ii.contents:
                if(content.find(special_tag)!=-1):
                    No_special_tag_found = False
            if(No_special_tag_found):
               item = ii.text
               Des_list.append(item)
        #  print(temp)
        #  print(Des_list)
         Func["Description"] = "\n".join(Des_list)
        #  print(Func["Description"])
        #  print("\n###################\n")
      ################################################################################################################
      ############################Pre and Post conditions#########################################
         Pre_PostConditionsFound("section pre" , "Precondition")
         Pre_PostConditionsFound("section post" , "Postcondition")
        #  print(Func["Precondition"]) 
        #  print(Func["Postcondition"]) 
      ################################################################################################################
      ############################Return Des#########################################
         Func["ReturnDes"] = i.find("div" , {"class" : "memdoc"}).find("dl" , {"class" : "section return"}).find("dd").text
         if(Func["ReturnDes"]==""):
            Func["ReturnDes"] = " - "
        #  print(Func["ReturnDes"])
      ################################################################################################################
      ############################Parameters in out#########################################
         ParamIN_OUT_content = i.find("div" , {"class" : "memdoc"}).find("table" , {"class" : "params"})
         ParamIN_OUT_index = 1
         for ParamIN_OUT in ParamIN_OUT_content:
            if(ParamIN_OUT!="\n"):
                ParamIN_OUT_dir = ParamIN_OUT.find("td",{"class":"paramdir"}).text.strip()
                ParamIN_OUT_Name= ParamIN_OUT.find("td",{"class":"paramname"}).text.strip()
                ParamIN_OUT_Desc= ParamIN_OUT.find_all("td")[-1].text.strip()
                # print(ParamIN_OUT_dir , "\t\t" , ParamIN_OUT_Name , "\t\t" , ParamIN_OUT_Desc)
                if(ParamIN_OUT_dir == "[in]"):
                   Func["ParametersDes[in]"].append(f"({ParamIN_OUT_index}) " + ParamIN_OUT_Name + "\t" + ParamIN_OUT_Desc)
                   Func["ParametersDes[out]"].append(" - ")
                   ParamIN_OUT_index += 1
                elif(ParamIN_OUT_dir == "[out]"):
                   Func["ParametersDes[out]"] = f"({ParamIN_OUT_index}) " + ParamIN_OUT_Name + "\t" + ParamIN_OUT_Desc
                   Func["ParametersDes[in]"].append(" - ")
                # print(Func["ParametersDes[in]"])
      ################################################################################################################
      ############################HistoryOfChanges#########################################
         HistoryPart_content = i.find("div" , {"class" : "memdoc"}).find("table" , {"align":"left"} , {"style" : "width:800px"}).find_all("td")
         for Index in range(0,len(HistoryPart_content)-4,1):
            if(HistoryPart_content[Index].text.strip() in Func["HistoryOfChanges"].keys()):
               Func["HistoryOfChanges"][HistoryPart_content[Index].text.strip()] = HistoryPart_content[Index+4].text
        #  print(Func["HistoryOfChanges"])
         ModuleFunc_list.append(Func.copy())
      Func = {
       "FunctionName" : "" , #
       "return"       : "" , #
       "Params"       : [] , #
       "ReturnDes"    : "" , #
       "ParametersDes[in]"  : [] , #
       "ParametersDes[out]" : [] , #
       "Precondition" : "" , #
       "Postcondition": "" , #
       "Description"  : "" , #
       "HistoryOfChanges" : {
          "Date" : "" ,
          "Software Version" : "" ,
          "Initials" : "" ,
          "Description" : ""
       }
      }
    pprint(ModuleFunc_list)
    RowData["ModuleName"] = ModuleName
    RowData["fileType"]   = ModuleType
    RowData["Functions"]   = ModuleFunc_list
    Database = pandas.DataFrame(ModuleFunc_list)
    Database.to_excel("./Python/Doxgen_parsingTask/DoxData.xlsx",Database)
      
