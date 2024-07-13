import tkinter as tk
import customtkinter as ctk
from GUI_BaseDesign import BaseDesign , Configuration_container , root
from GUI_page2 import Page2

class Page1(BaseDesign):
    def __init__(self , NextBtnEnable , GenerationBtnEnable , progressBarVal ):
        super().__init__(NextBtnEnable , GenerationBtnEnable)
        self.FileType = tk.StringVar()
        self.FileType.set("none")
        self.progressBarVal = progressBarVal
        self.Page1_Creation()

    def Page1_Creation(self):
        self.progressBar.set(self.progressBarVal)
        ################ Label of Main Text ######################
        self.MainText("Select which file type you want to generate :" , self.MainText_frame)
        self.add_spacer(80 , self.Content_Frame )

        self.RadioButtons_frame = ctk.CTkFrame(master=self.Content_Frame , corner_radius=20 , fg_color= "white" 
                                        , bg_color="white" , width= 400 , height= 200)
        self.RadioButtons_frame.pack(anchor = 'w')
        self.RadioButtons_frame.pack_propagate(False)

        self.Class_RadioBtn  = ctk.CTkRadioButton(master=self.RadioButtons_frame , text = "Class"  , variable= self.FileType , 
                                        command=self.RadioButtonsAction ,value="Class"  , bg_color= "white" )
        self.Class_RadioBtn.pack(pady= 10 , padx = 10 , anchor = 'w')

        self.Module_RadioBtn = ctk.CTkRadioButton(master=self.RadioButtons_frame , text = "Module" , variable= self.FileType , 
                                        command=self.RadioButtonsAction ,value="Module" , bg_color= "white")
        self.Module_RadioBtn.pack(pady= 10 , padx = 10 , anchor = 'w')

    def Page1_destroy(self):
        self.RadioButtons_frame.destroy()
        super().Base_destroy()
       
    def RadioButtonsAction(self):
        self.Next_button.configure(state = "normal")
        Configuration_container["FileType"].append(self.FileType.get())
    
    def MainText(self , string , frame):
        MainText = ctk.CTkLabel(master= frame , text= string , font= ("Courier" , 14 , "bold"))
        MainText.pack(anchor = 'w')
    
    def add_spacer(self, size , frame) :
        Spacer_Frame = ctk.CTkFrame(master=frame , corner_radius=20 , fg_color= "white" , bg_color="white" , width= 300 , height=size)
        Spacer_Frame.pack(anchor = 'w' )
        Spacer_Frame.pack_propagate(False)
    
    def Next_ButtonAction(self):
        self.Page1_destroy()
        page2_instance = Page2("normal" , "disabled")
        self.progressBarVal = 0.33
        page2_instance.Page2_creation(self.FileType , self.progressBarVal)

    def Generate_ButtonAction(self):
        pass


def start(Next_btn_state = "disabled" , Generate_btn_state = "disabled" , ProgressBarValue = 0.2):
    Page1_init = Page1(Next_btn_state , Generate_btn_state , ProgressBarValue)

start()
root.mainloop()

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
