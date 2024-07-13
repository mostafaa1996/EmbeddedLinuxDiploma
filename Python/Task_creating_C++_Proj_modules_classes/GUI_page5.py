import tkinter as tk
import customtkinter as ctk
from GUI_BaseDesign import BaseDesign , Configuration_container , root
import Create_Cpp_Project_script as CppCreation

class Page5(BaseDesign):
    def __init__(self , NextBtnEnable , GenerationBtnEnable , progressBarVal ):
        super().__init__(NextBtnEnable , GenerationBtnEnable)
        self.FileType = tk.StringVar()
        self.FileType.set("none")
        self.progressBarVal = progressBarVal
        self.Page5_Creation()

    def Page5_Creation(self):
        self.progressBar.set(self.progressBarVal)
        ################ Label of Main Text ######################
        self.MainText("Generate or Make another files by pressing Next Button: " , self.MainText_frame)
        self.add_spacer(80 , self.Content_Frame )


    def Page5_destroy(self):
        super().Base_destroy()
    
    def MainText(self , string , frame):
        MainText = ctk.CTkLabel(master= frame , text= string , font= ("Courier" , 14 , "bold"))
        MainText.pack(anchor = 'w')
    
    def add_spacer(self, size , frame) :
        Spacer_Frame = ctk.CTkFrame(master=frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height=size)
        Spacer_Frame.pack(anchor = 'w' )
        Spacer_Frame.pack_propagate(False)
    
    def Next_ButtonAction(self):
        self.Page5_destroy()
        import GuI_page1 

    def Generate_ButtonAction(self):
        CppCreation.Generation()