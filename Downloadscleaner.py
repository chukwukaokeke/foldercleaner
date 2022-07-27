#!/usr/bin/env python3

import os
import shutil

user= os.path.expanduser("~") 
path= f"{user}/Downloads"
folderlist = ["PDF","Spreedsheet","Textfile","Executable","Misc."]


def makedirectory(directory):
    try:
        if os.path.isdir(directory) == False:
            os.chdir(path)
            os.mkdir(directory)
            print(f"The {folder} folder cleawas created...Files are being arranged...")
            
            
    except FileExistsError:  
        print("Folders already created. Files are being arranged...")  

for folder in folderlist:
    makedirectory(folder)     
    


for file in os.listdir(path):
    if file.endswith(".pdf"):
        shutil.move(f"{path}/{file}", f"{path}/PDF")
    elif file.endswith(".xlsx"):
        shutil.move(f"{path}/{file}", f"{path}/Spreedsheet")
    elif file.endswith(".docx"):
        shutil.move(f"{path}/{file}", f"{path}/Textfile")
    
    
    