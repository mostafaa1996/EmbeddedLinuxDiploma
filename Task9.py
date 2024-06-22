#!/usr/bin/python3
#Write python code to generate Init function of GPIO for AVR
from pprint import pprint
AVR_IO_PORT_Registers = {
    "PORTA" : {
        "DDRA"  : "0b00000000",
        "PORTA" : "0b00000000",
        "PINA"  : "0b00000000"
    },
    "PORTB" : {
        "DDRB"  : "0b00000000",
        "PORTB" : "0b00000000",
        "PINB"  : "0b00000000"
    },
    "PORTC" : {
        "DDRC"  : "0b00000000",
        "PORTC" : "0b00000000",
        "PINC"  : "0b00000000"
    },
    "PORTD" : {
        "DDRD"  : "0b00000000",
        "PORTD" : "0b00000000",
        "PIND"  : "0b00000000"
    }
}

##########CONFIGURATION##############
List_output_pins = []
List_INPUT_Pullup_pins = []
required_Ports = []
INPUT = ""
for i in AVR_IO_PORT_Registers :
    INPUT = (input(f"Enter your Next port needs to be configered from this list :-\n\
        {AVR_IO_PORT_Registers.keys()} or press G for generating Configuration now : "))
    if INPUT.lower() != 'g' :
        required_Ports.append(INPUT)
        List_output_pins.append(input("specify the pin number needs to be configured as output consecutively separated by spaces :").split(" "))
        List_INPUT_Pullup_pins.append(input("specify the pin number needs to be configured as pulled up consecutively separated by spaces :").split(" "))
    else: break
##########CONFIGURATION##############
print(required_Ports)
print(List_output_pins)
print(List_INPUT_Pullup_pins)
##########Assigning##################
for i in required_Ports :
    temp_list = list(AVR_IO_PORT_Registers[i.upper()]["DDR"+i[-1].upper()])
    for x in List_output_pins[required_Ports.index(i)]:
        temp_list[int(x)+2] = '1'
    temp_str = "".join(temp_list)
    AVR_IO_PORT_Registers[i.upper()]["DDR"+i[-1].upper()] = temp_str
    temp_list = list(AVR_IO_PORT_Registers[i.upper()]["PORT"+i[-1].upper()])
    for x in List_INPUT_Pullup_pins[required_Ports.index(i)]:
        temp_list[int(x)+2] = '1'
    temp_str = "".join(temp_list)
    AVR_IO_PORT_Registers[i.upper()]["PORT"+i[-1].upper()] = temp_str
##########Assigning##################
pprint(AVR_IO_PORT_Registers)
