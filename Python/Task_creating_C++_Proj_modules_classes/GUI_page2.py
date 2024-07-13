import tkinter as tk
import customtkinter as ctk
from GUI_BaseDesign import BaseDesign , Configuration_container
import Create_Cpp_Project_script as CppCreation
from GUI_page3 import Page3

class Page2(BaseDesign) :
    
    def __init__(self , NextBtnEnable , GenerationBtnEnable):
        super().__init__(NextBtnEnable , GenerationBtnEnable)
        self.FileName_TextBox = None
        self.Path_TextBox  = None
        self.FileType = ""
        self.progressBarVal = 0
  
    def Page2_creation(self , FileType , progressBarVal):
        self.FileType = FileType.get()
        self.progressBarVal = progressBarVal
        self.progressBar.set(self.progressBarVal)
        ################ Label of Main Text ######################
        self.MainText("Enter Name and Path of files : " , self.MainText_frame)
        self.add_spacer(80 , self.Content_Frame)
        self.FileName_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , 
                                    fg_color= "white" , bg_color="white" , width= 300 , height=100)
        self.FileName_frame.pack(anchor = 'w' )
        self.FileName_frame.pack_propagate(True)

        self.Path_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 ,
                                fg_color= "white" , bg_color="white" , width= 300 , height=100)
        self.Path_frame.pack(anchor = 'w' )
        self.Path_frame.pack_propagate(True)

        self.FileName_label = ctk.CTkLabel(master=self.FileName_frame , text=f"Enter {self.FileType} Name : " )
        self.FileName_label.pack(side = "left" , padx = 10 , anchor = 'nw')
        self.FileName_TextBox = ctk.CTkTextbox(master=self.FileName_frame , width= 250 , 
                                        height= 30 , bg_color="white" , border_color = "black" , border_width = 1)
        self.FileName_TextBox.pack(side = "left" , padx = 10 , anchor = 'ne')

        self.Path_label = ctk.CTkLabel(master=self.Path_frame , text=f"Enter preferred Path :  " )
        self.Path_label.pack(side = "left" , pady = 10 , padx = 10 , anchor = 'nw')
        self.Path_TextBox = ctk.CTkTextbox(master=self.Path_frame , width= 250 , height= 30 , 
                                    bg_color="white" , border_color = "black" , border_width = 1)
        self.Path_TextBox.pack(side = "left" , pady = 10 , padx = 10 , anchor = 'ne')
    
    def Page2_destroy(self):
        self.FileName_frame.destroy()
        self.Path_frame.destroy()
        super().Base_destroy()
    
    def ClassModuleNamePath(self):
        name = self.FileName_TextBox.get("1.0" , "end-1c")
        if self.FileType == "Class":
            CppCreation.Class["ClassName"] = name
        elif self.FileType == "Module":
            CppCreation.Module["Name"] = name
        MainPath = self.Path_TextBox.get("1.0","end-1c")
        while "\\" in MainPath:
            MainPath = MainPath.replace("\\", "/")   
        last_slash_index = MainPath.rfind("/")
        RootPath = MainPath[0 : last_slash_index]
        if(RootPath not in Configuration_container["Directories"]):
            Configuration_container["Directories"].append(RootPath)
        Configuration_container["Directories"].append(f"{MainPath}")
        Configuration_container["files"].append(f"{MainPath}/{name}.h") 
    
    def MainText(self , string , frame):
        MainText = ctk.CTkLabel(master= frame , text= string , font= ("Courier" , 14 , "bold"))
        MainText.pack(anchor = 'w')
    
    def add_spacer(self, size , frame) :
        Spacer_Frame = ctk.CTkFrame(master=frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height=size)
        Spacer_Frame.pack(anchor = 'w' )
        Spacer_Frame.pack_propagate(False)

    def Next_ButtonAction(self):
        self.ClassModuleNamePath()
        self.Page2_destroy()
        page3_instance = Page3("normal" , "disabled")
        self.progressBarVal = 0.5
        page3_instance.Page3_creation(self.FileType , self.progressBarVal)
    def Generate_ButtonAction():
        pass

        