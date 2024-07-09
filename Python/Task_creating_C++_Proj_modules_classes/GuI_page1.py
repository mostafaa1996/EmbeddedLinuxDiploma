import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

root = ctk.CTk()
root.geometry("500x400+600+600")
root.title("C/C++ FileCreator")
ctk.set_appearance_mode("system")

root.resizable(width=False , height=False)
root.config(bg="white")

FileType = tk.StringVar()
FileType.set("none")

def RadioButtonsAction():
    Next_button.configure(state = "normal")

def Next_ButtonAction():
    pass

def MainText(string):
    MainText_frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color= "gray" , bg_color="white" , width= 200 , height= 50)
    MainText_frame.grid(row = 4, rowspan = 2 , column = 0 , columnspan = 8 , pady = 10)
    MainText = ctk.CTkLabel(master= MainText_frame , text= string , font= ("Courier" , 14 , "bold")).pack(side = "left")

def Page1_Content():
    global FileType
################ Label of Main Text ######################
    MainText("Select which file type you want to generate :")
##########################################################
    RadioButtons_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height= 100)
    RadioButtons_frame.grid(row = 6 , rowspan=4  , column = 0 , columnspan = 8 , sticky = "w")
    Class_RadioBtn  = ctk.CTkRadioButton(master=RadioButtons_frame , text = "Class"  , variable=FileType , 
                                    command=RadioButtonsAction ,value="Class"  , bg_color= "white" ).pack(pady= 20 , padx = 20)
    Module_RadioBtn = ctk.CTkRadioButton(master=RadioButtons_frame , text = "Module" , variable=FileType , 
                                    command=RadioButtonsAction ,value="Module" , bg_color= "white").pack()
def Page2_Content():
    global FileType
################ Label of Main Text ######################
    MainText("Enter Name and Path of files : ")
##########################################################
    FileName_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
    FileName_frame.grid(row = 6 , rowspan=2  , column = 0 , columnspan = 8 , sticky = "we")
    Path_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
    Path_frame.grid(row = 8 , rowspan=2  , column = 0 , columnspan = 8 , sticky = "we")
    
    FileName_label = ctk.CTkLabel(master=FileName_frame , text=f"Enter {FileType} Name : " )
    FileName_label.pack(side = "left" , pady = 10 , padx = 10)
    FileName_TextBox = ctk.CTkTextbox(master=FileName_frame , width= 250 , height= 30 , bg_color="white" , border_color = "black" , border_width = 1)
    FileName_TextBox.pack(side = "left" , pady = 10 , padx = 10)

    Path_label = ctk.CTkLabel(master=Path_frame , text=f"Enter preferred Path :  " )
    Path_label.pack(side = "left" , pady = 10 , padx = 10)
    Path_TextBox = ctk.CTkTextbox(master=Path_frame , width= 250 , height= 30 , bg_color="white" , border_color = "black" , border_width = 1)
    Path_TextBox.pack(side = "left" , pady = 10 , padx = 10)

def Page3_Content():
    if FileType != "Class" :
################ Label of Main Text ######################
        MainText("Enter Class Data members(scope , type , name) : ")
##########################################################
        PlusBtn_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 200 , height=50)
        PlusBtn_frame.grid(row = 6 , rowspan=2  , column = 0 , columnspan = 8 , sticky = "we")
        plusBtn = ctk.CTkButton(master=PlusBtn_frame , text= " + " , font= ("Arial" , 14 , "bold"), width= 20 , height=20)
        plusBtn.pack(side = "left" , padx = 20 , pady = 10)
        
        DataEntry_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "gray" , bg_color="white" ,
                                       width= 200 , height=50)
        DataEntry_frame.grid(row = 8 , rowspan=2  , column = 0 , columnspan = 8 , sticky = "we")
        
        DataName_label = ctk.CTkLabel(master=DataEntry_frame , text="DataName:", bg_color="white", font=("Arial" , 14 , "bold"))
        DataName_label.pack(side = "left", padx = 5 , pady = 10)
        DataName_TextBox = ctk.CTkTextbox(master=DataEntry_frame , width= 80 , height= 30 , 
                                          bg_color="white" , border_color = "black" , border_width = 1)
        DataName_TextBox.pack(side = "left" , pady = 10 , padx = 5)
        
        DataType_label = ctk.CTkLabel(master=DataEntry_frame , text="DataType:", bg_color="white", font=("Arial" , 14 , "bold"))
        DataType_label.pack(side = "left", padx = 5 , pady = 10)
        DataType_ComboBox = ctk.CTkComboBox(master=DataEntry_frame , width= 80 , height= 30 , 
                                          bg_color="white" , border_color = "black" , border_width = 1)
        DataType_ComboBox.pack(side = "left" , pady = 10 , padx = 5)

        Scope_label = ctk.CTkLabel(master=DataEntry_frame , text="Scope:", bg_color="white", font=("Arial" , 14 , "bold"))
        Scope_label.pack(side = "left", padx = 5 , pady = 10)
        Scope_ComboBox = ctk.CTkComboBox(master=DataEntry_frame , width= 80 , height= 30 , 
                                        bg_color="white" , border_color = "black" , border_width = 1)
        Scope_ComboBox.pack(side = "left" , pady = 10 , padx = 5)
        
        DataContainer_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "gray" , bg_color="white" ,
                                       width= 200 , height=100)
        DataContainer_frame.grid(row = 10 ,rowspan = 4 , column = 0 , columnspan = 8 , sticky = "we")
        # DataContainer_label = ctk.CTkLabel(master=DataContainer_frame , text="DataContainer:", 
        #                                    bg_color="white", font=("Arial" , 14 , "bold"))
        
        # DataContainer_label.pack(side = "left" , padx = 10)

    elif FileType == "Module" : 
################ Label of Main Text ######################
        MainText("Enter Module`s Data (scope , type , name) : ")
##########################################################
   
################## Image Frame ###########################
Image_frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color= "gray" , bg_color="white" , width= 500 , height= 50)
Image_frame.grid(row = 0 , column = 0 , columnspan = 20 , rowspan=2 , sticky = "we")

pil_img = Image.open("./Python/Task_creating_C++_Proj_modules_classes/Blue.png")
resized_image = pil_img.resize((625, 60))
img = ImageTk.PhotoImage(resized_image)

Image_label = ctk.CTkLabel(master= Image_frame , image=img , text="" , width=500 , height=30 , 
                           bg_color="black" , anchor='w').pack(side = "left")
##########################################################

################ Content Area ######################
# Page1_Content()
# Page2_Content()
# Page3_Content()
##########################################################

################ Progress Area ###########################
Progress_frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height= 40)
Progress_frame.grid(row = 13 , rowspan=2  , column = 0 , columnspan = 10 , sticky = "we", pady = 130 , padx = 20)

title_label = ctk.CTkLabel(Progress_frame, text="Progress : ", font=("Arial", 16, "bold"))
title_label.pack(pady=5 , side = 'left')
progressBar = ctk.CTkProgressBar(master=Progress_frame , progress_color="green",width=200 , height=10 )
progressBar.set(0.1)
progressBar.pack(pady = 10 , side = 'left', padx = 5 )

Next_button = ctk.CTkButton(master=Progress_frame , text="Next" , font=("Arial", 16, "bold"),
                            corner_radius=15 , width= 50 , height=25 , state="disabled" , command=Next_ButtonAction)
Next_button.pack(side ="left" , pady = 10 , padx = 10 )

Generate_button = ctk.CTkButton(master=Progress_frame , text="Generate" , font=("Arial", 16, "bold"),
                            corner_radius=15 , width= 50 , height=25 , state="disabled" , command=Next_ButtonAction)
Generate_button.pack(side ="left" , pady = 10 )
#############################################################

root.mainloop()
