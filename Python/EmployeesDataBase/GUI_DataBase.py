import tkinter as tk 
import customtkinter as ctk
from PIL import Image, ImageTk
import itertools
import EmployeesDataBase_task as Em
############## Main Window Creation ##################
root = ctk.CTk()
root.geometry("500x600+400+400")
root.title("Employees DataBase Reader/Creator")
ctk.set_appearance_mode("system")
root.resizable(width=False , height=False)
root.config(bg="white")

######################################################
# 1 column = 25 , 1 row = 25
class BaseDesign():
    def __init__(self , ADDBtnEnable , GenerationBtnEnable , BackBtnState):
        self.OpenExcel_button = None
        self.ADD_button = None
        self.GenerateExcel_button = None
        self.ReadExcel_button = None
        self.Delete_button = None
        self.Modify_button = None
        self.MainText_frame = None
        self.Content_Frame = None
        self.Progress_frame = None
        self.loadingRead_label = None
        self.loadingWriting_label = None
        self.TrueSign_img = ImageTk.PhotoImage(Image.open("./Python/EmployeesDataBase/TrueSign.png").resize((30, 30)))
        self.BaseCreation(ADDBtnEnable , GenerationBtnEnable , BackBtnState)

    def BaseCreation(self , ADDBtnEnable ,GenerationBtnEnable , BackBtnState):
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
        MainText_label = tk.Label(self.MainText_frame, text="Add, remove or modify Your Employees Information :", font=("Helvetica", 12, "bold") , bg= "white")
        MainText_label.pack(anchor='w', pady=10)
        self.Content_Frame = ctk.CTkFrame(master=root , corner_radius=20 , fg_color= "white" , 
                                     bg_color="white" , width= 500 , height= 250)
        self.Content_Frame.grid(row = 4 , rowspan=10  , column = 0 , columnspan = 20 , sticky = "we")
        self.Content_Frame.pack_propagate(False)


        ################ Progress Area ###########################
        self.Progress_frame = tk.Frame(master=root , bg="white" , width= 500 , height= 150 , relief="groove" , borderwidth = 3 )
        self.Progress_frame.grid(row = 14 , rowspan=6  , column = 0 , columnspan = 20 , sticky = "we", pady=5, padx=20)
        self.Progress_frame.pack_propagate(False)

        title_label = tk.Label(self.Progress_frame, text="New Item", font=("Helvetica", 14, "bold") , bg= "white")
        title_label.pack(side="top")

        self.spacer1_frame = ctk.CTkFrame(master=self.Progress_frame , corner_radius=20 , fg_color= "white" , 
                                        bg_color="white" , width= 50 , height= 150)
        self.spacer1_frame.pack(anchor = 'w' , side = "left")
        self.spacer1_frame.pack_propagate(False)

        self.LoadingProcess(self.spacer1_frame)
        
        self.OpenExcel_button = ctk.CTkButton(master=self.Progress_frame , text="Open sheet" , font=("Arial", 16, "bold") ,
                            corner_radius=15 , width= 80 , height=30 , state=BackBtnState , command=self.openExcel_ButtonAction)
        self.OpenExcel_button.pack(side ="left" , pady = 10)

        self.ADD_button  = ctk.CTkButton(master=self.Progress_frame , text="ADD Item" , font=("Arial", 16, "bold"),
                            corner_radius=15 , width= 80 , height=30 , state=ADDBtnEnable , command=self.ADD_ButtonAction)
        self.ADD_button.pack(side ="left" , pady = 10 , padx = 10 )

        self.GenerateExcel_button = ctk.CTkButton(master=self.Progress_frame , text="Generate New Excel" , font=("Arial", 16, "bold"),
                                    corner_radius=15 , width= 80 , height=30 , state=GenerationBtnEnable , command=self.Generate_ButtonAction)
        self.GenerateExcel_button.pack(side ="left" , pady = 10 )

        self.ModificationFrame = tk.Frame(master=root , bg="white" , width= 500 , height= 150 , relief="groove" , borderwidth = 3 )
        self.ModificationFrame.grid(row = 20 , rowspan=6  , column = 0 , columnspan = 20 , sticky = "we" , pady=5, padx=20)
        self.ModificationFrame.pack_propagate(False)

        title2_label = tk.Label(self.ModificationFrame, text="Modify Item", font=("Helvetica", 14, "bold") , bg= "white")
        title2_label.pack(side="top", pady=10)

        self.spacer2_frame = ctk.CTkFrame(master=self.ModificationFrame , corner_radius=20 , fg_color= "white" , 
                                        bg_color="white" , width= 50 , height= 150)
        self.spacer2_frame.pack(anchor = 'w' , side = "left")
        self.spacer2_frame.pack_propagate(False)

        self.LoadingProcess(self.spacer2_frame)

        self.ReadExcel_button = ctk.CTkButton(master=self.ModificationFrame , text="Read From Excel" , font=("Arial", 16, "bold"),
                                    corner_radius=15 , width= 80 , height=30 , state=GenerationBtnEnable , command=self.Read_ButtonAction)
        self.ReadExcel_button.pack(side ="left" , pady = 10 )

        self.Delete_button = ctk.CTkButton(master=self.ModificationFrame , text="Delete Item" , font=("Arial", 16, "bold"),
                                    corner_radius=15 , width= 80 , height=30 , state=GenerationBtnEnable , command=self.Delete_ButtonAction)
        self.Delete_button.pack(side ="left" , pady = 10 , padx = 10)

        self.Modify_button = ctk.CTkButton(master=self.ModificationFrame , text="Modify Item" , font=("Arial", 16, "bold"),
                                    corner_radius=15 , width= 80 , height=30 , state=GenerationBtnEnable , command=self.Modify_ButtonAction)
        self.Modify_button.pack(side ="left" , pady = 10 )


    def ADD_ButtonAction():
        pass
    def Generate_ButtonAction():
        pass
    def openExcel_ButtonAction():
        pass
    def Read_ButtonAction():
        pass
    def Delete_ButtonAction():
        pass
    def Modify_ButtonAction():
        pass    
    def Base_destroy(self):
        self.Progress_frame.destroy()
        self.MainText_frame.destroy()
        self.Content_Frame.destroy()

    def LoadingFrame(self , frame_iterator , label):
        try:
            frame = next(frame_iterator)
            label.config(image=frame)
            root.after(100, self.LoadingFrame, frame_iterator , label)
        except:
            pass
    
    def LoadingProcess(self , root):
        self.loadingRead_label = tk.Label(master=root , fg="white" , bg= "white" )
        self.loadingRead_label.grid(row=22 , column=0)
        loading_frames = [ImageTk.PhotoImage(Image.open(f"./Python/EmployeesDataBase/loading{i}.png").resize((30, 30))) for i in range(1, 6)] 
        frame_iterator = itertools.cycle(loading_frames)
        self.LoadingFrame(frame_iterator , self.loadingRead_label)

class Core_design(BaseDesign):
    def __init__(self, ADDBtnEnable, GenerationBtnEnable, BackBtnState):
        super().__init__(ADDBtnEnable, GenerationBtnEnable, BackBtnState)
        self.EmployeeName = None
        self.EmployeeTitle = None
        self.EmployeeID = None
        self.EmployeeSalary = None
        self.EmployeeFrame = None
        self.arrayOfTextBoxes = []
        self.arrayOfTextBoxesIndex = 0
        self.NameTrueSign = None
        self.TitleTrueSign = None
        self.IDTrueSign = None
        self.SalaryTrueSign = None
        self.arrayOfLabelsWithTrueSign = []
        self.PlusBtn = None
        self.Core_design_Creator()

    def Core_design_Creator(self):
        self.EmployeeFrame = tk.Frame(master=self.Content_Frame , borderwidth = 3 , bg= "white" , width=500 , height=200 , relief="groove" )
        self.EmployeeFrame.pack(pady=5, padx=20, fill="both", expand=True)
        title_label = tk.Label(self.EmployeeFrame, text="Employee Information", font=("Helvetica", 16, "bold") , bg= "white")
        title_label.pack(side="top", pady=5)
        self.EmployeeNameFrame = tk.Frame(master=self.EmployeeFrame  , bg= "white" , width=550 , height=40 )
        self.EmployeeNameFrame.pack(anchor='w', pady=10 )
        self.EmployeeNameFrame.pack_propagate(False)
        self.EmployeeTitleFrame = tk.Frame(master=self.EmployeeFrame  , bg= "white" , width=550 , height=40 )
        self.EmployeeTitleFrame.pack(anchor='w')
        self.EmployeeTitleFrame.pack_propagate(False)
        self.EmployeeIDFrame = tk.Frame(master=self.EmployeeFrame  , bg= "white" , width=550 , height=40 )
        self.EmployeeIDFrame.pack(anchor='w', pady=10)
        self.EmployeeIDFrame.pack_propagate(False)
        self.EmployeeSalaryFrame = tk.Frame(master=self.EmployeeFrame  , bg= "white" , width=550 , height=40 )
        self.EmployeeSalaryFrame.pack(anchor='w')
        self.EmployeeSalaryFrame.pack_propagate(False)
        self.PlusBtn = ctk.CTkButton(master=self.EmployeeFrame , width= 40 , height=40 , text= "+" , 
                                     font=("Helvetica", 16, "bold") , command=self.PlusBtnEvent , state="disabled")
        self.PlusBtn.pack(padx = 10 , anchor = 'w')
        
        self.EmployeeName_label     = tk.Label(master=self.EmployeeNameFrame , text = "Employee Name" , font= ("Helvetica", 12, "bold"), bg= "white")
        self.EmployeeTitle_label    = tk.Label(master=self.EmployeeTitleFrame , text = "Employee Title" , font= ("Helvetica", 12, "bold"), bg= "white")
        self.EmployeeID_label       = tk.Label(master=self.EmployeeIDFrame , text = "Employee ID" , font= ("Helvetica", 12, "bold"), bg= "white")
        self.EmployeeSalar_label    = tk.Label(master=self.EmployeeSalaryFrame , text = "Employee Salar" , font= ("Helvetica", 12, "bold"), bg= "white")
        self.EmployeeName_TextBox   = ctk.CTkTextbox(master=self.EmployeeNameFrame , width= 200 , height= 5  
                                                     , wrap="word" , border_color= "black" , border_width=2)
        self.EmployeeName_TextBox.focus_set()
        self.EmployeeTitle_TextBox  = ctk.CTkTextbox(master=self.EmployeeTitleFrame , width= 200 , height= 5  
                                                     , wrap="word" , border_color= "black" , border_width=2)
        self.EmployeeID_TextBox     = ctk.CTkTextbox(master=self.EmployeeIDFrame , width= 200 , height= 5  
                                                     , wrap="word" , border_color= "black" , border_width=2)
        self.EmployeeSalary_TextBox = ctk.CTkTextbox(master=self.EmployeeSalaryFrame , width= 200 , height= 5 
                                                     , wrap="word", border_color= "black" , border_width=2 )
        self.arrayOfTextBoxes = [self.EmployeeName_TextBox , self.EmployeeTitle_TextBox 
                                 , self.EmployeeID_TextBox , self.EmployeeSalary_TextBox]
        self.EmployeeName_label    .pack(anchor='w', padx= 10 , side= "left")
        self.EmployeeTitle_label   .pack(anchor='w', padx= 10 , side= "left")
        self.EmployeeID_label      .pack(anchor='w', padx= 10 , side= "left")
        self.EmployeeSalar_label   .pack(anchor='w', padx= 10 , side= "left")
        self.EmployeeName_TextBox  .pack(anchor='w', padx= 10 , side= "left" ,  expand=True)
        self.EmployeeTitle_TextBox .pack(anchor='w', padx= 20 , side= "left" ,  expand=True)
        self.EmployeeID_TextBox    .pack(anchor='w', padx= 30 , side= "left" ,  expand=True)
        self.EmployeeSalary_TextBox.pack(anchor='w', padx= 11 , side= "left" ,  expand=True)

        self.NameTrueSign = tk.Label(master=self.EmployeeNameFrame ,  bg= "white" , fg="white")
        self.TitleTrueSign = tk.Label(master=self.EmployeeTitleFrame , bg= "white" , fg="white")
        self.IDTrueSign = tk.Label(master=self.EmployeeIDFrame ,  bg= "white" , fg="white")
        self.SalaryTrueSign = tk.Label(master=self.EmployeeSalaryFrame , bg= "white" , fg="white")
        self.arrayOfLabelsWithTrueSign = [self.NameTrueSign , self.TitleTrueSign , self.IDTrueSign , self.SalaryTrueSign]
        self.arrayOfTextBoxes[0].bind("<Control_L>", self.TextBoxAction)

    def ADD_ButtonAction(self):
        Em.AddItemToexisting_Excel()
    def Generate_ButtonAction(self):
        Em.Generate_Excel()
    def openExcel_ButtonAction(self):
        Em.Open_Excel()
    def Read_ButtonAction(self):
        Em.Read_Excel()
    def Delete_ButtonAction(self):
        Em.RemoveItemsIn_Excel
    def Modify_ButtonAction(self):
        Em.ModifyItemsIn_Excel() 

    def PlusBtnEvent(self):
        Em.Employee_Info["Name"] = self.EmployeeName_TextBox.get("1.0" , "end-1c")
        Em.Employee_Info["Title"] = self.EmployeeTitle_TextBox.get("1.0" , "end-1c")
        Em.Employee_Info["ID"] = self.EmployeeID_TextBox.get("1.0" , "end-1c")
        Em.Employee_Info["Salary"] = self.EmployeeSalary_TextBox.get("1.0" , "end-1c")
        self.EmployeeName_TextBox.delete("1.0","end-1c")
        self.EmployeeTitle_TextBox.delete("1.0","end-1c")
        self.EmployeeID_TextBox.delete("1.0","end-1c")
        self.EmployeeSalary_TextBox.delete("1.0","end-1c")
        self.arrayOfTextBoxesIndex = 0
        for i in self.arrayOfLabelsWithTrueSign:
            i.config(image="")
        self.GenerateExcel_button.configure(state = "normal")
        self.ADD_button.configure(state = "normal")

    def TextBoxAction(self , event=None):
        if(self.arrayOfTextBoxesIndex < len(self.arrayOfTextBoxes)-1):
            self.arrayOfTextBoxes[self.arrayOfTextBoxesIndex+1].bind("<Control_L>", self.TextBoxAction)
            self.arrayOfTextBoxes[self.arrayOfTextBoxesIndex+1].focus_set()
        if(self.arrayOfTextBoxes[self.arrayOfTextBoxesIndex].get("1.0","end-1c") != ""):
            self.arrayOfLabelsWithTrueSign[self.arrayOfTextBoxesIndex].config(image=self.TrueSign_img)
            self.arrayOfLabelsWithTrueSign[self.arrayOfTextBoxesIndex].pack(anchor='e' , side= "left" , padx= 10)
        self.arrayOfTextBoxesIndex+=1
        self.Delete_button.configure(state = "normal")
        self.Modify_button.configure(state = "normal")
        self.ReadExcel_button.configure(state = "normal")
        self.PlusBtn.configure(state = "normal")
        if(self.arrayOfTextBoxesIndex == 4):
            self.arrayOfTextBoxesIndex = 0
            

        
UI = Core_design("disabled" , "disabled" , "normal")
root.mainloop()