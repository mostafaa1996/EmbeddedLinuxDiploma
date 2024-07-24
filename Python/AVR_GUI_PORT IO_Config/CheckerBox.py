import customtkinter as ctk
import tkinter as tk


class checkerBox():
    def __init__(self, MasterFrame , num , dark_bg_color) -> None:
        self.CheckBox = None
        self.littleFrame = None
        self.var = tk.IntVar()
        self.CreateSelectionSpace(MasterFrame , num , dark_bg_color)

    def CreateSelectionSpace(self , MasterFrame , num , dark_bg_color):
        self.littleFrame = ctk.CTkFrame(master=MasterFrame , corner_radius=15 , fg_color=dark_bg_color , 
                                        bg_color=dark_bg_color , width= 40 , height= 80)
        self.littleFrame.pack(side="left" , padx = 5 , pady = 5)

        self.CheckBox = ctk.CTkCheckBox(master=self.littleFrame , width=5 , height=5 , command=self.checker_Event , text=str(num) , variable=self.var)
        self.CheckBox.pack()

    def checker_Event(self):
        pass

