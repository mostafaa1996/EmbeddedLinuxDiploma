import tkinter as tk
import customtkinter as ctk
from GUI_BaseDesign import BaseDesign 
import Create_Cpp_Project_script as CppCreation
from pprint import pprint
from GUI_page5 import Page5

class Page4(BaseDesign):
    def __init__(self , NextBtnEnable , GenerationBtnEnable):
        super().__init__(NextBtnEnable , GenerationBtnEnable)
        self.PlusBtn_frame = None
        self.plusBtn = None
        self.FuncName_TextBox = None
        self.Scope_ComboBox  = None
        self.MainFrame = None
        self.General_frame = None
        self.Parameters_TextBox = None
        self.functionContainer = None
        self.ReturnType_ComboBox = None
        self.name = ""
        self.ReturnType = ""
        self.Parameters = ""
        self.scope_list = []
        self.progressBarVal = 0
        self.FileType = ""
        

    def Page4_creation(self , FileType , ProgressVal):
        self.progressBarVal = ProgressVal
        self.FileType = FileType
        self.progressBar.set(self.progressBarVal)
        if self.FileType == "Class" :
            ################ Label of Main Text ######################
            self.MainText("Enter Class Method members(scope , type , name) : " ,  self.MainText_frame)
        elif self.FileType == "Module" : 
            ################ Label of Main Text ######################
            self.MainText("Enter Module`s Functions (scope , type , name) : " ,  self.MainText_frame)

        self.PlusBtn_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 500 , height=50)
        self.PlusBtn_frame.pack(anchor = "w" , pady = 5)
        self.PlusBtn_frame.pack_propagate(False)

        self.plusBtn = ctk.CTkButton(master=self.PlusBtn_frame , text= " + " , font= ("Arial" , 14 , "bold")
                                     , width= 30 , height=30 , command= self.plusBtnEvent)
        self.plusBtn.pack(anchor = 'w' , padx = 5 , side = "left")

        self.DataName_label = ctk.CTkLabel(master=self.PlusBtn_frame , text="FunctionName:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.DataName_label.pack(side = "left", padx = 5 )
        self.FuncName_TextBox = ctk.CTkTextbox(master=self.PlusBtn_frame , width= 160 , height= 30 , 
                                        bg_color="white" , border_color = "black" , border_width = 1)
        self.FuncName_TextBox.pack(side = "left" , padx = 5)

        self.Scope_label = ctk.CTkLabel(master=self.PlusBtn_frame , text="Scope:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.Scope_label.pack(side = "left", padx = 5 )
        self.Scope_ComboBox = ctk.CTkComboBox(master=self.PlusBtn_frame , width= 80 , height= 30 , 
                                    bg_color="white" , border_color = "black" , border_width = 1)
        self.Scope_ComboBox.pack(side = "left" , padx = 5)
        if(self.FileType == "Class"):
          self.Scope_ComboBox.configure(values = ["private" , "protected" , "public"]) 
        else :
          self.Scope_ComboBox.configure(values = ["static" , "volatile" , " "]) 
        ###########################################################################################################################
        self.MainFrame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 500 , height=50)
        self.MainFrame.pack(anchor = "w" )
        self.MainFrame.pack_propagate(False)

        self.ReturnType_frame = ctk.CTkFrame(master=self.MainFrame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
        self.ReturnType_frame.pack( anchor = "w" , side = "left")
        self.ReturnType_frame.pack_propagate(False)

        self.otherType_frame = ctk.CTkFrame(master= self.MainFrame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
        self.otherType_frame.pack(anchor = "w" , side = "left" , padx = 10 )
        self.otherType_frame.pack_propagate(False)

        self.ReturnType_label = ctk.CTkLabel(master=self.ReturnType_frame , text="ReturnType:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.ReturnType_label.pack(side = "left", padx = 5 )
        self.ReturnType_ComboBox = ctk.CTkComboBox(master=self.ReturnType_frame , width= 120 , height= 30 , 
                                        bg_color="white" , border_color = "black" ,
                                        border_width = 1 , command=self.ReturnType_ComboBoxEvent
                    , values = ["None" , "char" , "int" , "float" , "double" , "unsigned int" , "unsigned char" , "CustomType"])
        self.ReturnType_ComboBox.pack(side = "left" , padx = 5)

        self.other_label = ctk.CTkLabel(master=self.otherType_frame , text="ReturnType:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.other_label.pack(side = "left", padx = 5 )
        self.other_TextBox = ctk.CTkTextbox(master=self.otherType_frame , width= 120 , height= 30 , 
                              bg_color="white" , border_color = "black" , border_width = 1 , state = "disabled")
        self.other_TextBox.pack(side = "left" , padx = 5)


        self.General_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" ,
                                    width= 500 , height=125)
        self.General_frame.pack(anchor = "w" , pady = 10 )
        self.General_frame.pack_propagate(False)


        self.Params_frame = ctk.CTkFrame(master=self.General_frame , corner_radius=20 , fg_color= "white" , bg_color="white" ,
                                    width= 200 , height=125)
        self.Params_frame.pack(padx = 20 , side="left")
        self.Params_frame.pack_propagate(False)

        self.functionContainer_frame = ctk.CTkFrame(master=self.General_frame , corner_radius=20 , fg_color= "white" , bg_color="white" ,
                                    width= 200 , height=125)
        self.functionContainer_frame.pack(side="left")
        self.functionContainer_frame.pack_propagate(False)

        self.functionContainer_label = ctk.CTkLabel(master=self.functionContainer_frame , text="FunctionContainer:", 
                                        bg_color="white", font=("Arial" , 14 , "bold"))
        self.functionContainer_label.pack(anchor = 'nw' , padx = 5)
        self.functionContainer = tk.Listbox(master= self.functionContainer_frame , width= 200 , height= 100 )
        self.functionContainer.pack()

        self.Parameters_label = ctk.CTkLabel(master=self.Params_frame , text="Parameters:", 
                                        bg_color="white", font=("Arial" , 14 , "bold"))
        self.Parameters_label.pack(anchor = 'nw' , padx = 5)
        self.Parameters_TextBox = ctk.CTkTextbox(master= self.Params_frame , width= 200 , height= 100 )
        self.Parameters_TextBox.pack()

    def Page4_destroy(self):
        self.PlusBtn_frame.destroy()
        self.MainFrame.destroy()
        self.General_frame.destroy()
        super().Base_destroy()

    def plusBtnEvent(self):
        self.name = self.FuncName_TextBox.get("1.0" , "end-1c")
        if self.ReturnType_ComboBox.get() == "CustomType" :
            self.ReturnType = self.other_TextBox.get("1.0" , "end-1c") 
        Temp_str = self.Parameters_TextBox.get("1.0" , "end-1c")
        self.Parameters = f"({Temp_str})"
        Temp_str = ""
        if self.FileType == "Class":
            self.scope_list.append(self.Scope_ComboBox.get())
            Temp_str = f"{self.ReturnType} {self.name}{self.Parameters}"
            self.functionContainer.insert('end' , Temp_str)
        elif self.FileType== "Module":
            scope_str = self.Scope_ComboBox.get()
            Temp_str = f"{scope_str} {self.ReturnType} {self.name}{self.Parameters}"
            self.functionContainer.insert('end' , Temp_str)
        self.name = ""
        self.ReturnType = ""
        self.FuncName_TextBox.clipboard_clear()
        self.ReturnType_ComboBox.clipboard_clear()
        self.other_TextBox.clipboard_clear()
        self.other_TextBox.configure(state = "disabled")
        self.Scope_ComboBox.clipboard_clear()
        self.FuncName_TextBox.delete("1.0", "end")
        self.ReturnType_ComboBox.set("")
        self.other_TextBox.delete("1.0", "end")
        self.Scope_ComboBox.set("")
        

    def ReturnType_ComboBoxEvent(self , value):
        if value == "CustomType" :
            self.other_TextBox.configure(state = "normal")
        else:
            self.ReturnType = value

    def MainText(self , string , frame):
        MainText = ctk.CTkLabel(master= frame , text= string , font= ("Courier" , 14 , "bold"))
        MainText.pack(anchor = 'w')
    
    def add_spacer(self, size , frame) :
        Spacer_Frame = ctk.CTkFrame(master=frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height=size)
        Spacer_Frame.pack(anchor = 'w' )
        Spacer_Frame.pack_propagate(False)

    def Next_ButtonAction(self):
        if self.FileType == "Module":
            CppCreation.Module["Functions"] = self.functionContainer.get(0, tk.END)
        elif self.FileType == "Class":
            i=0
            Func_list = self.functionContainer.get(0, tk.END)
            for Datascope in self.scope_list :
                CppCreation.Class["Method_members"][Datascope].append(Func_list[i])
                i+=1
        CppCreation.Configuration_container["Classes"].append(CppCreation.Class)
        CppCreation.Configuration_container["Modules"].append(CppCreation.Module)
        CppCreation.Class = {
            "ClassName" : "" , 
            "Constructors" : [] , 
            "Data_members" : {"private" : [] , "protected" : [] , "public" : []},
            "Method_members" : {"private" : [] , "protected" : [] , "public" : []}
        }
        CppCreation.Module= {'Name' : "" ,"Data" : [] , "Functions" : []}
        self.Page4_destroy()
        self.progressBarVal = 1
        page5_instance = Page5("normal" , "normal" , self.progressBarVal)
        pprint(CppCreation.Configuration_container)

    def Generate_ButtonAction():
        pass