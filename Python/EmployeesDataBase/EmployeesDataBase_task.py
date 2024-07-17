from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import openpyxl as xl
import pandas as pd
import os 

Employee_Info = {('Employees Information',"Name") : "" , ('Employees Information',"Title") : "" ,
                 ('Employees Information',"ID") : ""   , ('Employees Information',"Salary") : "" }
Employees_list_ToBe_write = []
Employees_list_ToBe_Read = []
openedExcelSheet = None
fileName = ""

def Generate_Excel():
    DataBase = pd.DataFrame(Employees_list_ToBe_write)
    multiindex = pd.MultiIndex.from_tuples(DataBase.columns, names=['Employees Information' , 'Attributes'])
    DataBase.columns = multiindex
    f = asksaveasfile(initialfile = 'Untitled.xlsx',
        defaultextension=".xlsx",filetypes=[("All Files","*.*"),("Excel Format","*.xlsx")])
    print(f.name)
    DataBase.to_excel(f.name)
    
def Read_Excel():
    file = fd.askopenfile()
    book = xl.load_workbook(file.name)
    sheet = book.active
    rows_data = []

    # Get the headers from the first row
    headers = [cell.value for cell in next(sheet.iter_rows(min_row=2, max_row=2))]

    # Iterate over the remaining rows and convert each row to a dictionary
    for row in sheet.iter_rows(min_row=3, values_only=True):
        row_data = dict(zip(headers, row))
        rows_data.append(row_data.copy())
    for i in rows_data :
        i.pop("Attribute")
    print(rows_data)
    file.close()
    Employees_list_ToBe_Read = rows_data.copy()

def ModifyItemsIn_Excel():
    pass

def RemoveItemsIn_Excel():
    pass

def AddItemToexisting_Excel():
    global Employee_Info
    Employees_list_ToBe_write.append(Employee_Info.copy())

def Open_Excel():
    global fileName
    file = fd.askopenfile()
    fileName = file.name
    file.close()
    
def appendToOpenedExcel():
    global fileName
    DataBase = pd.DataFrame(Employees_list_ToBe_write)
    book = xl.load_workbook(fileName)
    sheet = book.active
    # Append new rows
    for row in DataBase.itertuples(index=True, name=None):
        sheet.append(row)

    # Save the workbook
    book.save(fileName)
    




