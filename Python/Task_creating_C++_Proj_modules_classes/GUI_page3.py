import tkinter as tk
import customtkinter as ctk
from GUI_BaseDesign import BaseDesign , Class , Module
from GUI_page4 import Page4


class Page3(BaseDesign):
    def __init__(self , NextBtnEnable , GenerationBtnEnable):
        super().__init__(NextBtnEnable , GenerationBtnEnable)
        self.plusBtn = None
        self.DataName_TextBox = None
        self.Scope_ComboBox = None
        self.DataType_ComboBox = None
        self.other_TextBox = None
        self.DataContainer = None
        self.name = ""
        self.type = ""
        self.scope = ""
        self.initialValue = "0"
        self.MainFrame = None
        self.DataContainer_frame = None
        self.PlusBtn_frame = None
        self.scope_list = []
        self.FileType = None
        self.progressBarVal = None
        

    def Page3_creation(self , FileType , progressBarVal):
        self.FileType = FileType
        self.progressBarVal = progressBarVal
        self.progressBar.set(self.progressBarVal)
        if self.FileType == "Class" :
            ################ Label of Main Text ######################
            self.MainText("Enter Class Data members(scope , type , name) : " ,  self.MainText_frame)

        elif self.FileType == "Module" : 
            ################ Label of Main Text ######################
            self.MainText("Enter Module`s Data (scope , type , name) : " ,  self.MainText_frame)

        self.PlusBtn_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 500 , height=50)
        self.PlusBtn_frame.pack(anchor = "w" , pady = 5)
        self.PlusBtn_frame.pack_propagate(False)

        self.plusBtn = ctk.CTkButton(master=self.PlusBtn_frame , text= " + " , font= ("Arial" , 14 , "bold")
                                     , width= 30 , height=30 , command= self.plusBtnEvent)
        self.plusBtn.pack(padx = 5 , side = "left")

        self.DataName_label = ctk.CTkLabel(master=self.PlusBtn_frame , text="DataName:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.DataName_label.pack(padx = 5 , side = "left")
        self.DataName_TextBox = ctk.CTkTextbox(master=self.PlusBtn_frame , width= 120 , height= 30 , 
                                           bg_color="white" , border_color = "black" , border_width = 1)
        self.DataName_TextBox.pack(padx = 5 , side = "left")

        self.Scope_label = ctk.CTkLabel(master=self.PlusBtn_frame , text="Scope:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.Scope_label.pack(padx = 5 , side = "left")
        self.Scope_ComboBox = ctk.CTkComboBox(master=self.PlusBtn_frame , width= 150 , height= 30 , 
                                       bg_color="white" , border_color = "black" , 
                                       border_width = 1 , command= self.Scope_ComboBoxEvent)
        self.Scope_ComboBox.pack(side = "left" , padx = 5)
        if(self.FileType == "Class"):
          self.Scope_ComboBox.configure(values = ["private" , "protected" , "public"]) 
        else :
          self.Scope_ComboBox.configure(values = ["static" , "volatile" , " "]) 
        ##################################################################################################################################################
        self.MainFrame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 500 , height=50)
        self.MainFrame.pack(anchor = "w" )
        self.MainFrame.pack_propagate(False)

        self.DataType_frame = ctk.CTkFrame(master= self.MainFrame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
        self.DataType_frame.pack(anchor = "w" , side = "left")
        self.DataType_frame.pack_propagate(False)

        self.otherType_frame = ctk.CTkFrame(master= self.MainFrame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
        self.otherType_frame.pack(anchor = "w" , side = "left" , padx = 10 )
        self.otherType_frame.pack_propagate(False)

        self.DataType_label = ctk.CTkLabel(master=self.DataType_frame , text="DataType:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.DataType_label.pack(side = "left", padx = 5 )
        self.DataType_ComboBox = ctk.CTkComboBox(master=self.DataType_frame , width= 120 , height= 30 , 
                                            bg_color="white" , border_color = "black" , border_width = 1 
                                            , command=self.DataType_ComboBoxEvent 
        , values = ["None" , "char" , "int" , "float" , "double" , "unsigned int" , "unsigned char" , "CustomType"])
        self.DataType_ComboBox.pack(side = "left" , padx = 20)

        self.other_label = ctk.CTkLabel(master=self.otherType_frame , text="CustomType:", bg_color="white", font=("Arial" , 14 , "bold"))
        self.other_label.pack(side = "left", padx = 5 )
        self.other_TextBox = ctk.CTkTextbox(master=self.otherType_frame , width= 120 , height= 30 , 
                                bg_color="white" , border_color = "black" , border_width = 1 , state = "disabled")
        self.other_TextBox.pack(side = "left" , padx = 20)

        ##################################################################################################################################################
        self.DataContainer_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" , bg_color="white" ,
                                        width= 500 , height=100)
        self.DataContainer_frame.pack(anchor = "w" , pady = 10 )
        self.DataContainer_frame.pack_propagate(False)
        self.DataContainer_label = ctk.CTkLabel(master= self.DataContainer_frame , text="DataContainer:", 
                                            bg_color="white", font=("Arial" , 14 , "bold"))

        self.DataContainer_label.pack(anchor = 'n' , side = "left" , padx = 5)
        self.DataContainer = tk.Listbox(master= self.DataContainer_frame , width= 350 , height= 100 )
        self.DataContainer.pack(side = "left" , padx = 20 , anchor = 'ne')

    def DataType_ComboBoxEvent(self , value):
        if value == "CustomType" :
            self.other_TextBox.configure(state = "normal")
        else :
            self.type = value

    def Scope_ComboBoxEvent(self , value):
        pass

    def plusBtnEvent(self):
        self.name = self.DataName_TextBox.get("1.0" , "end-1c")
        self.scope = self.Scope_ComboBox.get()
        if self.DataType_ComboBox.get() == "CustomType" :
            self.type = self.other_TextBox.get("1.0" , "end-1c")
        if self.FileType =="Module":
            Temp_str = f"{self.scope} {self.type} {self.name} = {self.initialValue}"
            self.DataContainer.insert('end' , Temp_str)
        if self.FileType =="Class":
            Temp_str = f"{self.type} {self.name} = {self.initialValue}"
            self.DataContainer.insert('end' , Temp_str)
            self.scope_list.append(self.scope)
        self.name = ""
        self.scope = ""
        self.type = ""
        self.DataName_TextBox.clipboard_clear()
        self.DataType_ComboBox.clipboard_clear()
        self.other_TextBox.clipboard_clear()
        self.other_TextBox.configure(state = "disabled")
        self.Scope_ComboBox.clipboard_clear()
        self.DataName_TextBox.delete("1.0", "end")
        self.DataType_ComboBox.set("")
        self.other_TextBox.delete("1.0", "end")
        self.Scope_ComboBox.set("")

    def Page3_destroy(self):
        self.MainFrame.destroy()
        self.DataContainer_frame.destroy()
        self.PlusBtn_frame.destroy()
        super().Base_destroy()
    
    def MainText(self , string , frame):
        MainText = ctk.CTkLabel(master= frame , text= string , font= ("Courier" , 14 , "bold"))
        MainText.pack(anchor = 'w')
    
    def add_spacer(self, size , frame) :
        Spacer_Frame = ctk.CTkFrame(master=frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height=size)
        Spacer_Frame.pack(anchor = 'w' )
        Spacer_Frame.pack_propagate(False)
    
    def Next_ButtonAction(self):
        if self.FileType == "Module":
            Module["Data"] = self.DataContainer.get(0,tk.END)
        elif self.FileType == "Class":
            DataContainerList = self.DataContainer.get(0, tk.END)
            if len(DataContainerList)> 0:
                Class["Constructors"] = ['1' , '2']
            i=0
            for Datascope in self.scope_list :
                Class["Data_members"][Datascope].append(DataContainerList[i])
                i+=1
        self.Page3_destroy()
        page4_instance = Page4("normal" , "disabled")
        self.progressBarVal = 0.8
        page4_instance.Page4_creation(self.FileType , self.progressBarVal)

    def Generate_ButtonAction():
        pass