import tkinter as tk 
import customtkinter as ctk
from PIL import Image, ImageTk
from Create_Cpp_Project_script import Configuration_container , Class , Module

############## Main Window Creation ##################
root = ctk.CTk()
root.geometry("500x450+400+400")
root.title("C/C++ FileCreator")
ctk.set_appearance_mode("system")
root.resizable(width=False , height=False)
root.config(bg="white")

######################################################
# 1 column = 25 , 1 row = 25
class BaseDesign():
    def __init__(self , NextBtnEnable , GenerationBtnEnable):
        self.progressBar = None
        self.Next_button = None
        self.Generate_button = None
        self.MainText_frame = None
        self.Content_Frame = None
        self.Progress_frame = None
        self.FileType = None
        self.BaseCreation(NextBtnEnable , GenerationBtnEnable)

    def BaseCreation(self , NextBtnEnable ,GenerationBtnEnable):
        ################## Blue Image Frame ###########################
        self.Image_frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color= "white" ,
                                    bg_color="white" , width= 500 , height= 50)
        self.Image_frame.grid(row = 0 , column = 0 , columnspan = 20 , rowspan=2 , sticky = "we")

        pil_img = Image.open("./Python/Task_creating_C++_Proj_modules_classes/Blue.png")
        resized_image = pil_img.resize((625, 60))
        img = ImageTk.PhotoImage(resized_image)

        self.Image_label = ctk.CTkLabel(master= self.Image_frame , image=img , text="" , width=500 , height=30 , 
                                bg_color="black" , anchor='w').pack(side = "left")


        ################### Content Frame ###########################
        self.MainText_frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color= "white" , 
                                      bg_color="white" , width= 400 , height= 50)
        self.MainText_frame.grid(row = 2, rowspan = 2 , column = 0 , columnspan = 16  , sticky = "we")
        self.Content_Frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , 
                                     bg_color="white" , width= 500 , height= 250)
        self.Content_Frame.grid(row = 4 , rowspan=10  , column = 0 , columnspan = 20 , sticky = "we")
        self.Content_Frame.pack_propagate(False)


        ################ Progress Area ###########################
        self.Progress_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , 
                                        bg_color="white" , width= 500 , height= 100)
        self.Progress_frame.grid(row = 14 , rowspan=4  , column = 0 , columnspan = 10 , sticky = "we")
        self.Progress_frame.pack_propagate(False)
        self.title_label = ctk.CTkLabel(self.Progress_frame, text="Progress : ", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5 , padx = 10 , side = 'left')
        self.progressBar = ctk.CTkProgressBar(master=self.Progress_frame , progress_color="green",width=200 , height=10 )
        self.progressBar.set(0.1)
        self.progressBar.pack(pady = 10 , side = 'left', padx = 5 )

        self.Next_button = ctk.CTkButton(master=self.Progress_frame , text="Next" , font=("Arial", 16, "bold"),
                            corner_radius=15 , width= 50 , height=25 , state=NextBtnEnable , command=self.Next_ButtonAction)
        self.Next_button.pack(side ="left" , pady = 10 , padx = 10 )

        self.Generate_button = ctk.CTkButton(master=self.Progress_frame , text="Generate" , font=("Arial", 16, "bold"),
                                    corner_radius=15 , width= 50 , height=25 , state=GenerationBtnEnable , command=self.Generate_ButtonAction)
        self.Generate_button.pack(side ="left" , pady = 10 )

    def Next_ButtonAction():
        pass
    def Generate_ButtonAction():
        pass
    def Base_destroy(self):
        self.Progress_frame.destroy()
        self.MainText_frame.destroy()
        self.Content_Frame.destroy()

