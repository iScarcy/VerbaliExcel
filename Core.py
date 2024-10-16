import time
from tkinter import ttk
import os

def elabora(inputPath : str,outputPath : str, fileComuni : str, pb : ttk.Progressbar):
   
    files = os.listdir(inputPath) 
    num_file : int = len(files) 
    increment = 100 // num_file
    if increment > 0:
        pb.pack()
        for filename in files:
            if filename.endswith(".xlsx") or filename.endswith(".xls"): 
                print(filename)
                pb["value"] += increment 
                continue
            else:
                continue

    

    pb.stop    
    