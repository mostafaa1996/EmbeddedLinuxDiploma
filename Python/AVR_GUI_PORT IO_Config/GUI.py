#!/usr/bin/python3
#Write python code to generate Init function of GPIO for AVR
import customtkinter as ctk
import tkinter as tk
import CheckerBox as CB

AVR_IO_PORT_Registers = {
    "PORTA" : {
        "DDRA"  : [0,0,0,0,0,0,0,0],
        "PORTA" : [0,0,0,0,0,0,0,0],
        
    },
    "PORTB" : {
        "DDRB"  : [0,0,0,0,0,0,0,0],
        "PORTB" : [0,0,0,0,0,0,0,0],
        
    },
    "PORTC" : {
        "DDRC"  : [0,0,0,0,0,0,0,0],
        "PORTC" : [0,0,0,0,0,0,0,0],
    },
    "PORTD" : {
        "DDRD"  : [0,0,0,0,0,0,0,0],
        "PORTD" : [0,0,0,0,0,0,0,0],
    }
}

root = ctk.CTk()
root.geometry("1200x600+200+200")
root.title("AVR PORT IO Configuration")
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root.resizable(width=True , height=True)
dark_bg_color = root.cget("bg")
PORTA_CheckBOX_InOut_List = []
PORTA_CheckBOX_PullUpDown_List = []
PORTB_CheckBOX_InOut_List = []
PORTB_CheckBOX_PullUpDown_List = []
PORTC_CheckBOX_InOut_List = []
PORTC_CheckBOX_PullUpDown_List = []
PORTD_CheckBOX_InOut_List = []
PORTD_CheckBOX_PullUpDown_List = []

def Generate_ButtonAction():
    global AVR_IO_PORT_Registers
    for i in range(8):
      AVR_IO_PORT_Registers["PORTA"]["DDRA"][i]  = str(PORTA_CheckBOX_InOut_List[i].var.get())
      AVR_IO_PORT_Registers["PORTA"]["PORTA"][i] = str(PORTA_CheckBOX_PullUpDown_List[i].var.get())
      AVR_IO_PORT_Registers["PORTB"]["DDRB"][i]  = str(PORTB_CheckBOX_InOut_List[i].var.get())
      AVR_IO_PORT_Registers["PORTB"]["PORTB"][i] = str(PORTB_CheckBOX_PullUpDown_List[i].var.get())
      AVR_IO_PORT_Registers["PORTC"]["DDRC"][i]  = str(PORTC_CheckBOX_InOut_List[i].var.get())
      AVR_IO_PORT_Registers["PORTC"]["PORTC"][i] = str(PORTC_CheckBOX_PullUpDown_List[i].var.get())
      AVR_IO_PORT_Registers["PORTD"]["DDRD"][i]  = str(PORTD_CheckBOX_InOut_List[i].var.get())
      AVR_IO_PORT_Registers["PORTD"]["PORTD"][i] = str(PORTD_CheckBOX_PullUpDown_List[i].var.get())
    with open("./Python/AVR_GUI_PORT IO_Config/DIO.c" , "+w")as file:
        ddra  = "".join(AVR_IO_PORT_Registers["PORTA"]["DDRA"])
        porta = "".join(AVR_IO_PORT_Registers["PORTA"]["PORTA"])
        ddrb  = "".join(AVR_IO_PORT_Registers["PORTB"]["DDRB"])
        portb = "".join(AVR_IO_PORT_Registers["PORTB"]["PORTB"])
        ddrc  = "".join(AVR_IO_PORT_Registers["PORTC"]["DDRC"])
        portc = "".join(AVR_IO_PORT_Registers["PORTC"]["PORTC"])
        ddrd  = "".join(AVR_IO_PORT_Registers["PORTD"]["DDRD"])
        portd = "".join(AVR_IO_PORT_Registers["PORTD"]["PORTD"])
        file.write("#include \"Dio.h\" \n\n")
        file.write("void DIOInit(){\n")
        file.write("    DDRA = 0b")
        file.write(f"{ddra}\n")
        file.write("    PORTA = 0b")
        file.write(f"{porta}\n")
        file.write("    DDRB = 0b")
        file.write(f"{ddrb}\n")
        file.write("    PORTB = 0b")
        file.write(f"{portb}\n")
        file.write("    DDRC = 0b")
        file.write(f"{ddrc}\n")
        file.write("    PORTC = 0b")
        file.write(f"{portc}\n")
        file.write("    DDRD = 0b")
        file.write(f"{ddrd}\n")
        file.write("    PORTD = 0b")
        file.write(f"{portd}\n")
        file.write("}\n")

def deploying(frame1):
    List = []
    SPACER = ctk.CTkFrame(master=frame1 , corner_radius=15 , fg_color=dark_bg_color , 
                                        bg_color=dark_bg_color , width= 50 , height= 80)
    SPACER.pack(side="left" , padx = 5 , pady = 5)
    for i in range(8):
        checkObject = CB.checkerBox(frame1 ,i , dark_bg_color)
        List.append(checkObject)
    return List


def createOuterFrames(MainFrame , PadX , anchorVal , Text):
    Frame = ctk.CTkFrame(master=MainFrame , corner_radius=20 , fg_color=dark_bg_color , 
                                bg_color=dark_bg_color , width= 500 , height= 190 , border_color="#0000FF", border_width=1 )
    Frame.pack(side = "left" , anchor = anchorVal , padx = PadX ,pady = 5)
    Frame.pack_propagate(False)

    PORTA_label = tk.Label(master=Frame, text=Text, font=("Helvetica", 14, "bold") , bg=dark_bg_color , fg = "#0000FF")
    PORTA_label.pack()

    return Frame

def CreateInnerFrames(Frame):
    Frame1 = ctk.CTkFrame(master=Frame , corner_radius=20 , fg_color=dark_bg_color , 
                                    bg_color=dark_bg_color , width= 500 , height= 70 )
    Frame1.pack(padx = 5)
    Frame1.pack_propagate(False)

    label = tk.Label(master=Frame1, text="IN/OUT", font=("Helvetica", 14, "bold") , bg=dark_bg_color , fg = "#0000FF")
    label.pack(pady=5)

    Frame2 = ctk.CTkFrame(master=Frame , corner_radius=20 , fg_color=dark_bg_color , 
                                    bg_color=dark_bg_color , width= 500 , height= 70 )
    Frame2.pack(padx = 5)
    Frame2.pack_propagate(False)

    label = tk.Label(master=Frame2, text="PULL UP/DOWN", font=("Helvetica", 14, "bold") , bg=dark_bg_color , fg = "#0000FF")
    label.pack()

    return Frame1 , Frame2
    

MainText_frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color=dark_bg_color , bg_color=dark_bg_color , width= 1200 , height= 50)
MainText_frame.grid(row = 0, rowspan = 2 , column = 0 , columnspan = 48  , sticky = "we" , pady=20)
MainText_frame.pack_propagate(False)

MainText_label = tk.Label(MainText_frame, text="Configure your I/O PORT : ", font=("Helvetica", 12, "bold") , bg=dark_bg_color , fg = "blue")
MainText_label.pack(anchor='w', pady=10)

Content_Frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color=dark_bg_color , bg_color=dark_bg_color , width= 1200 , height= 400)
Content_Frame.grid(row = 2 , rowspan=16  , column = 0 , columnspan = 48 , sticky = "we")
Content_Frame.pack_propagate(False)

Generate_Frame = ctk.CTkFrame(master=root , corner_radius=15 , fg_color=dark_bg_color , bg_color=dark_bg_color , width= 1200 , height= 70)
Generate_Frame.grid(row = 18 , rowspan=3  , column = 0 , columnspan = 48 , sticky = "we", pady = 10)
Generate_Frame.pack_propagate(False)

Generate_button = ctk.CTkButton(master=Generate_Frame , text="Generate" , font=("Arial", 16, "bold") ,
                            corner_radius=15 , width= 100 , height=50 , state="normal" , command=Generate_ButtonAction)
Generate_button.pack()

####################################split content frame into two frames######################
PORTS1_Frame = ctk.CTkFrame(master=Content_Frame , corner_radius=20 , fg_color=dark_bg_color , 
                                bg_color=dark_bg_color , width= 1200 , height= 180)
PORTS1_Frame.pack(pady = 5)
PORTS1_Frame.pack_propagate(False)

PORTS2_Frame = ctk.CTkFrame(master=Content_Frame , corner_radius=20 , fg_color=dark_bg_color , 
                                bg_color=dark_bg_color , width= 1200 , height= 180)
PORTS2_Frame.pack(pady = 5)
PORTS2_Frame.pack_propagate(False)

####################################Port Area#################################################

PORTA_Frame = createOuterFrames(PORTS1_Frame , 45 , 'w' , "PORTA : ")
PORTB_Frame = createOuterFrames(PORTS1_Frame , 20 , 'e' , "PORTB : ")
PORTC_Frame = createOuterFrames(PORTS2_Frame , 45 , 'w' , "PORTC : ")
PORTD_Frame = createOuterFrames(PORTS2_Frame , 20 , 'e' , "PORTD : ")

####################################Inside Port area##########################################

PORTA1_Frame , PORTA2_Frame = CreateInnerFrames(PORTA_Frame)
PORTB1_Frame , PORTB2_Frame = CreateInnerFrames(PORTB_Frame)
PORTC1_Frame , PORTC2_Frame = CreateInnerFrames(PORTC_Frame)
PORTD1_Frame , PORTD2_Frame = CreateInnerFrames(PORTD_Frame)

PORTA_CheckBOX_InOut_List = deploying(PORTA1_Frame)
PORTA_CheckBOX_PullUpDown_List = deploying(PORTA2_Frame)
PORTB_CheckBOX_InOut_List = deploying(PORTB1_Frame)
PORTB_CheckBOX_PullUpDown_List = deploying(PORTB2_Frame)
PORTC_CheckBOX_InOut_List = deploying(PORTC1_Frame)
PORTC_CheckBOX_PullUpDown_List = deploying(PORTC2_Frame)
PORTD_CheckBOX_InOut_List = deploying(PORTD1_Frame)
PORTD_CheckBOX_PullUpDown_List = deploying(PORTD2_Frame)

##############################################################################################



root.mainloop()